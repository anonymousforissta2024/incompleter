from path_config import DATA_DIR, LOG_DIR
from main.utils.session import Session

import ast
from main.utils.snippet import Snippet
from main.utils.session import Session
from main.errors.error_coordinator import ErrorCoordinator
import json
import os
import re
import sys
import shutil
from subprocess import Popen, PIPE

ref_path = os.path.join(DATA_DIR, 'new_all/dataset3/assignments_info.json')
res_path = os.path.join(DATA_DIR, 'type_inference/res_inc_type.json')

refs = {}
with open(ref_path, 'r') as ref_file:
    ref = json.load(ref_file)
    for (ref_no, ref_dict) in ref.items():
        refs[ref_no] = {
            ref_dict['variable']: ref_dict['type']
        }

#---------------------------------------------------------------------------------------------------------------

# Deduces the type of a class based on several deductions
def analyze_code_to_unroll_dict(code):
    class TypeInferrer(ast.NodeVisitor):
        def __init__(self):
            self.unroll_dict = {}
            self.current_class = None
            self.class_methods = {}
            self.class_attributes = {}
            self.class_container_init = {}

            class UserDefinedClassVisitor(ast.NodeVisitor):
                def __init__(self):
                    self.current_class = None
                    self.user_defined_classes = {}

                def visit_ClassDef(self, node):
                    if 'TBD' not in node.name:
                        self.current_class = node.name
                        self.user_defined_classes[node.name] = {'class_methods': []}
                        for child in node.body:
                            self.visit(child)
                    return node

                def visit_FunctionDef(self, node):
                    if self.current_class in self.user_defined_classes.keys() and node.name != '__init__':
                        self.user_defined_classes[self.current_class]['class_methods'].append(node.name)
                    return node

            self.udc_visitor = UserDefinedClassVisitor()
            self.udc_visitor.visit(ast.parse(code))

        def visit_ClassDef(self, node):
            if 'TBD' in node.name:
                self.current_class = node.name
                # self.unroll_dict[node.name] = {'deductions': [], 'type': 'unknown'}
                base_classes = [base.id for base in node.bases if isinstance(base, ast.Name)] 
                self.unroll_dict[node.name] = {
                    'deductions': [],
                    'type': 'unknown',
                    'base_classes': base_classes
                }
                self.class_methods[node.name] = []
                self.class_attributes[node.name] = {}
                self.generic_visit(node)
                self.infer_class_type(node.name)
                self.current_class = None

        def visit_FunctionDef(self, node):
            if self.current_class:
                self.class_methods[self.current_class].append(node.name)
            self.generic_visit(node)

        def visit_Assign(self, node):
            if self.current_class and isinstance(node.targets[0], ast.Attribute) and \
            isinstance(node.targets[0].value, ast.Name) and \
            node.targets[0].value.id == 'self' and node.targets[0].attr == 'container':
                self.class_container_init[self.current_class] = node.value

        def is_user_defined(self, class_name):
            for (udc, udc_info) in self.udc_visitor.user_defined_classes.items():
                if any(method in self.class_methods[class_name] for method in udc_info['class_methods']):
                    self.unroll_dict[class_name]['deductions'].append('user-defined')
                    self.unroll_dict[class_name]['type'] = udc
                    break

        def is_primitive(self, class_name):
            deductions = self.unroll_dict[class_name]['deductions']
            base_classes = self.unroll_dict[class_name].get('base_classes', [])

            # Check for direct inheritance from primitive types
            if 'int' in base_classes:
                deductions.append(f'{class_name} subclasses int')
                self.unroll_dict[class_name]['type'] = 'int'
            elif 'str' in base_classes:
                deductions.append(f'{class_name} subclasses str')
                self.unroll_dict[class_name]['type'] = 'str'

            # check for string unique methods
            string_methods = ['capitalize', 'casefold', 'center', 'count', 'encode',
                        'endswith', 'expandtabs', 'find', 'format', 'format_map',
                        'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
                        'isdigit', 'isidentifier', 'islower', 'isnumeric',
                        'isprintable', 'isspace', 'istitle', 'isupper', 'join',
                        'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
                        'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
                        'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
                        'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

            if any(method in self.class_methods[class_name] for method in string_methods):
                deductions.append('implements string-specific methods')
                self.unroll_dict[class_name]['type'] = 'str'

        def mock_container_keys(self, class_name):
            container_node = self.class_container_init.get(class_name, None)
            if container_node and isinstance(container_node, ast.Dict):
                # Extract keys from the dictionary assignment
                keys = [key.value for key in container_node.keys if isinstance(key, ast.Constant)]
                return keys
            return None

        def is_collection(self, class_name):
            essential_methods = ['__init__', '__iter__', '__len__', '__getitem__', '__setitem__']
            methods = self.class_methods[class_name]
            deductions = self.unroll_dict[class_name]['deductions']

            # Retrieve the keys from the 'container' attribute, if it exists
            container_keys = self.mock_container_keys(class_name)

            # Check if any unique methods are implemented
            if any(method in methods for method in ['append', 'extend', 'insert', 'remove', 'index', 'count', 'sort', 'reverse']):
                deductions.append('implements list-specific methods')
                self.unroll_dict[class_name]['type'] = 'list'
            elif any(method in methods for method in ['get', 'items', 'keys', 'popitem', 'setdefault', 'update', 'values']):
                deductions.append('implements dict-specific methods')
                self.unroll_dict[class_name]['type'] = 'dict'
            elif any(method in methods for method in ['add', 'discard', 'union', 'intersection', 'difference', 'symmetric_difference', 
                                                    'intersection_update', 'difference_update', 'symmetric_difference_update']):
                deductions.append('implements set-specific methods')
                self.unroll_dict[class_name]['type'] = 'set'

            # Parse through container keys to determine type if no unique methods are implemented
            elif container_keys:
                if all(isinstance(key, int) for key in container_keys) and \
                        sorted(container_keys) == list(range(min(container_keys), max(container_keys)+1)):
                    deductions.append('key structure suggests list-like behavior')
                    self.unroll_dict[class_name]['type'] = 'list'
                else:
                    # Check if any of the keys is a TBD#, then the that TBD# is likely a str
                    for key in container_keys:
                        if isinstance(key, str) and 'TBD' in key and key in self.unroll_dict.keys():
                            deductions.append('appears as a key in another TBDIterableOrSubscriptable')
                            self.unroll_dict[key]['type'] = 'str'

                    deductions.append('key structure suggests dict-like behavior')
                    self.unroll_dict[class_name]['type'] = 'dict'
            elif all(method in methods for method in essential_methods):
                deductions.append('defaulting to list due to general format and absence of unique collection methods')
                self.unroll_dict[class_name]['type'] = 'list'
            else:
                return

        def is_callable(self, class_name):
            if '__call__' in self.class_methods[class_name]:
                self.unroll_dict[class_name]['deductions'].append(f'{class_name} implements __call__, marking as callable')
                self.unroll_dict[class_name]['type'] = 'callable'

        def infer_class_type(self, class_name):
            self.is_user_defined(class_name)
            if self.unroll_dict[class_name]['type'] == 'unknown':
                self.is_primitive(class_name)
            if self.unroll_dict[class_name]['type'] == 'unknown':
                self.is_collection(class_name)
            if self.unroll_dict[class_name]['type'] == 'unknown':
                self.is_callable(class_name)
            if self.unroll_dict[class_name]['type'] == 'unknown':
                self.unroll_dict[class_name]['deductions'].append('no specific type patterns recognized')
                self.unroll_dict[class_name]['type'] = 'object'

    tree = ast.parse(code)
    inferrer = TypeInferrer()
    inferrer.visit(tree)
    return inferrer.unroll_dict, inferrer.class_container_init

def extract_initialization_expression(node, type_str):
    if type_str == 'dict':
        keys = [ast.unparse(k).strip() for k in getattr(node, 'keys', []) if k is not None]
        values = [ast.unparse(v).strip() for v in getattr(node, 'values', []) if v is not None]
        
        if keys and values and len(keys) == len(values):
            items = [f"{k}: {v}" for k, v in zip(keys, values)]
            return "{" + ", ".join(items) + "}"
        else:
            return "{}"
    elif type_str in ['list', 'set']:
        values = [ast.unparse(v).strip() for v in getattr(node, 'values', []) if v is not None]
        
        if type_str == 'list':
            return "[" + ", ".join(values) + "]"
        else:  
            return "{" + ", ".join(values) + "}"
    if type_str == 'dict':
        return "{}"
    elif type_str == 'list':
        return "[]"
    elif type_str == 'set':
        return "set()"

def apply_single_replacement(code_snippet, class_name, type_info, class_container_init):
    """
    Apply a single replacement based on the inferred type information.
    Args:
        code_snippet (str): The current state of the code snippet.
        class_name (str): The name of the class to replace.
        type_info (dict): The inferred type information for the class.
        class_container_init (dict): Initializations of class containers.
    
    Returns:
        (str, bool): Tuple of the updated code snippet and a flag indicating success.
    """
    # Determine the replacement based on the inferred type
    if type_info['type'] in ['list', 'dict', 'set']:
        replacement = extract_initialization_expression(class_container_init.get(class_name, ast.Dict()), type_info['type'])
    elif type_info['type'] == 'int':
        replacement = '1'
    elif type_info['type'] == 'str':
        replacement = '""'
    else:
        return code_snippet, False 
    
    updated_code_snippet = code_snippet.replace(f"{class_name}()", replacement)

    return updated_code_snippet

def remove_unused_classes(code_snippet):
    """
    Remove class definitions that are no longer needed in the code snippet.
    
    Args:
        code_snippet (str): The current state of the code snippet after replacements.
    
    Returns:
        str: The cleaned-up code snippet.
    """
    class InstantiationTracker(ast.NodeVisitor):
        def __init__(self, **kwargs):
            self.tbd_name = kwargs['tbd_name']
            self.is_instantiated = False

        def visit_Call(self, node):
            if isinstance(node.func, ast.Name):
                if self.tbd_name == node.func.id:
                    self.is_instantiated = True

    tree = ast.parse(code_snippet)
    tbd_list = [node.name for node in reversed(tree.body) if isinstance(node, ast.ClassDef) and 'TBD' in node.name]
    
    for tbd in tbd_list:
        tracker = InstantiationTracker(tbd_name = tbd)
        tracker.visit(tree)

        new_body = []
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and node.name == tbd and not tracker.is_instantiated:
                pass
            else:
                new_body.append(node)
        
        tree.body = new_body
    
    return ast.unparse(ast.fix_missing_locations(tree))

def test_snippet(snippet_obj, updated_code_snippet):
    """
    Test the updated code snippet for functionality.
    
    Args:
        snippet_obj (Snippet): The Snippet object being tested.
        updated_code_snippet (str): The updated code snippet after applying a single replacement.
    
    Returns:
        bool: True if the snippet runs successfully (no errors), False otherwise.
    """
    snippet_obj.history[-1] = updated_code_snippet
    
    try:
        out, err, cov_summary, stmt_cov, br_cov = snippet_obj.compute_timed_latest_coverage()
        
        # Check if there are errors in the execution
        if err is None:
            # Timeout
            return False, None, None
        else:
            if len(err) > 0:
                err_coord = ErrorCoordinator(path=snippet_obj.snippet_path, snippet=snippet_obj, stack_trace=err)
                if len(err_coord.err_type):
                    return False, None, None
                else:
                    return True, stmt_cov, br_cov
            else:
                return True, stmt_cov, br_cov
    except Exception as e:
        return False, None, None
    finally:
        snippet_obj.history.pop()

class TBDAssociationFinder(ast.NodeVisitor):
    """
    This AST Node Visitor will find associations with TBD objects for record keeping
    """
    def __init__(self, preprocessed_tbds=[]):
        self.associations = {}
        self.preprocessed_tbds = preprocessed_tbds  

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == 'self':
                attribute_name = target.attr
                value_str = ast.unparse(node.value).strip()
                tbd_matches = re.findall(r'TBD\d+', value_str)
                for tbd_name in tbd_matches:
                    if tbd_name not in self.preprocessed_tbds:  # Check if TBD is preprocessed
                        self.associations[attribute_name] = {'type': 'object', 'tbd_name': tbd_name}
            elif isinstance(target, ast.Name):
                value_str = ast.unparse(node.value).strip()
                tbd_matches = re.findall(r'TBD\d+', value_str)
                for tbd_name in tbd_matches:
                    # print("PREPROCESSED TBDS")
                    # print(self.preprocessed_tbds)
                    # print("TBD NAME")
                    # print(tbd_name)
                    if tbd_name not in self.preprocessed_tbds:  # Check if TBD is preprocessed
                        self.associations[target.id] = {'type': 'object', 'tbd_name': tbd_name}
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        for stmt in node.body:
            if isinstance(stmt, ast.Return) and stmt.value:
                return_str = ast.unparse(stmt.value).strip()
                tbd_matches = re.findall(r'TBD\d+', return_str)
                for tbd_name in tbd_matches:
                    if tbd_name not in self.preprocessed_tbds: 
                        self.associations[node.name] = {'type': 'callable', 'tbd_name': tbd_name}
        self.generic_visit(node)

def find_tbd_associations(code_snippet, preprocessed_tbds):
    tree = ast.parse(code_snippet)
    finder = TBDAssociationFinder(preprocessed_tbds=preprocessed_tbds)
    finder.visit(tree)
    return finder.associations

def update_incompleter_info(snippets_info, associations):
    """
    Updates the incompleter_predicted_type in snippets_info based on associations found.
    """
    for identifier, associated_type in associations.items():
        for snippet in snippets_info:
            if identifier in snippet['identifiers']:
                snippet['identifiers'][identifier]['incompleter_predicted_type'] = associated_type
            else:
                snippet['identifiers'][identifier] = {
                    "lexecutor_predicted_type": "did not implement",
                    "incompleter_predicted_type": associated_type
                }

def find_associations_types(current_snippet_info, associations, unroll_dict):
    """
    Updates the incompleter_predicted_type in current_snippet_info based on associations and unroll_dict.
    """
    for identifier, info in associations.items():
        tbd_name = info['tbd_name'].replace('()', '').strip()  # Remove parentheses for matching

        if tbd_name in unroll_dict:
            inferred_type = unroll_dict[tbd_name]['type']

            if info['type'] == 'callable':
                inferred_type = "callable"
            elif inferred_type == "object" and info['type'] == 'object':
                inferred_type = "object"

            if identifier in current_snippet_info['identifiers']:
                current_snippet_info['identifiers'][identifier]['incompleter_predicted_type'] = inferred_type
            else:
                current_snippet_info['identifiers'][identifier] = {
                    "lexecutor_predicted_type": "did not implement",
                    "incompleter_predicted_type": inferred_type
                }
        else:
            current_snippet_info['identifiers'][identifier]['incompleter_predicted_type'] = "does not deduce this"

def fuzz(snippet_obj, code_snippet, class_name, info, class_container_init, unroll_dict):
    original_type = info['type']
    if original_type == 'list':
        # Temporarily change to list for the fuzz attempt
        info['type'] = 'dict'
        updated_code_snippet = apply_single_replacement(code_snippet, class_name, info, class_container_init)
        success = test_snippet(snippet_obj, updated_code_snippet)
        if success:
            # Keep list type change
            unroll_dict[class_name] = info
            info['deductions'] = ['fuzzed from list to dict']
            return True, updated_code_snippet
        else:
            # Revert changes if unsuccessful
            info['type'] = original_type
            unroll_dict[class_name] = info
    return False, None

def extract_prediction(predicted_str):
    '''
    Matches specific types from lexecutor model
    '''
    if "None" in predicted_str: return "None", 'NoneType'
    elif "True" in predicted_str: return "True", 'bool'
    elif "False" in predicted_str: return "False", 'bool'
    elif "-1.0" == predicted_str: return "-1.0", 'float'
    elif "0.0" == predicted_str: return "0.0", 'float'
    elif "1.0" == predicted_str: return "1.0", 'float'
    elif "-1" == predicted_str: return "-1", 'int'
    elif "0" == predicted_str: return "0", 'int'
    elif "1" == predicted_str: return "1", 'int'
    elif "a" == predicted_str: return "\"a\"", 'str'
    elif "" == predicted_str: return "", 'str'
    elif "[<" in predicted_str: return "[DummyObject()]", 'list'
    elif "[]" in predicted_str: return "[]", 'list'
    elif "{<" in predicted_str: return "\{DummyObject()\}", 'set'
    elif "{'a'" in predicted_str: return "\"a\": \{DummyObject()\}", 'dict'
    elif "(<" in predicted_str: return "(DummyObject())", 'tuple'
    elif "<class 'lexecutor.ValueAbstraction.DummyObject'>" in predicted_str: return 'callable', 'callable'
    elif "<lexecutor.ValueAbstraction.DummyObject" in predicted_str: return 'object', 'object'
    elif "<lexecutor.ValueAbstraction.DummyResource" in predicted_str: return "DummyResource()", 'resource'
    else: return 'object', 'object'

def run_lexecutor(snippet_obj):
    pred_map = {}

    src_path = snippet_obj.snippet_path.replace('.orig', '')
    dest_path = snippet_obj.tmp_path.replace('.orig', '')
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dest_path)
    else:
        return None
    proc = Popen(['python3', dest_path], stdout=PIPE, stderr=PIPE, cwd=snippet_obj.tmp_dir)
    out, err = proc.communicate(timeout=Snippet.TIMEOUT)
    out, err = out.decode('ISO-8859-1'), err.decode('ISO-8859-1')
    if len(err) == 0:
        return None
    else:
        # print(err)
        prediction_pattern = re.compile(r": Predicting for (name|attribute) (.*?):(.*)")
        predictions = prediction_pattern.findall(err)

        for prediction_type, identifier, predicted_raw_type in predictions:
            # print(f"Matched prediction for '{identifier}': '{predicted_raw_type}'")
            
            if identifier in snippet_obj.mocked_values.keys():
                predicted_value, predicted_type = extract_prediction(predicted_raw_type.strip())
                pred_map[snippet_obj.mocked_values[identifier]] = (predicted_value, predicted_type)
    return pred_map

def cross_check(snippet_obj, pred_map, tbd):
    s_prime = snippet_obj.get_latest()
    if tbd in pred_map.keys():
        if pred_map[tbd][1] in ['NoneType', 'bool', 'float', 'int', 'str'] or pred_map[tbd][0] == '[]':
            s_prime = s_prime.replace(f"{tbd}()", pred_map[tbd][0])
        elif pred_map[tbd][1] in ['list', 'set', 'tuple', 'dict']:
            if 'class DummyObject()' not in s_prime:
                s_prime = 'class DummyObject():\n\tdef __init__(self, *a, **b):\n\t\tpass\n' + s_prime
            s_prime = s_prime.replace(f"{tbd}()", pred_map[tbd][0])    
        return s_prime, pred_map[tbd][1]
    return s_prime, None

def prepare_context(mocked_snippet, snippet_obj, tbd):
    tree = ast.parse(mocked_snippet)
    tbd_class_def = ''
    tbd_refs = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == tbd:
            new_body = []
            for child in node.body:
                if isinstance(child, ast.FunctionDef) and child.name == '__init__':
                    new_body.append(child)
                elif isinstance(child, ast.FunctionDef) and '__' in child.name:
                    pass
                else:
                    new_body.append(child)
            node.body = new_body
            tbd_class_def = ast.unparse(ast.fix_missing_locations(node))
    class ReferenceFinder(ast.NodeVisitor):
        def __init__(self, **kwargs):
            self.identifier = kwargs['identifier']
            self.references = []
        def visit_Name(self, node):
            if node.id == self.identifier:
                self.references.append(mocked_snippet.split('\n')[node.lineno-1])
    
    if tbd in snippet_obj.tbd_tracker.keys():
        ref_finder = ReferenceFinder(identifier=snippet_obj.tbd_tracker[tbd])
        ref_finder.visit(tree)
        tbd_refs = list(ref_finder.references)

    return tbd_class_def + '\n' + '\n'.join(tbd_refs)

def query_inctp(mocked_snippet, snippet_obj, tbd):
    context = prepare_context(mocked_snippet, snippet_obj, tbd)
    test_in = 'classify type: {}: {}'.format(tbd, context)

    input_ids = Session.tokenizer(test_in, return_tensors="pt").input_ids
    generated_ids = Session.model.generate(input_ids, max_length=100, num_beams=25, early_stopping=True)
    generated_text = Session.tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    return generated_text

def unmock_code_snippet(snippet_obj, coverage_report, executability=True):
    """
    Analyzes the given code snippet, applies type deductions to replace class instantiations,
    and removes unused class definitions.

    Args:
        snippet_obj (Snippet): The Snippet object to analyze and update.

    Returns:
        str: The updated code snippet.
        dict: deduction tally of what deductions were successful
    """
    print('\nSTARTED UNMOCKING\n')
    code_snippet = snippet_obj.get_latest()
    unroll_dict, class_container_init = analyze_code_to_unroll_dict(code_snippet)
    tbd_associations = find_tbd_associations(code_snippet, snippet_obj.preprocessed_tbds)

    if Session.lextp:
        print("LexTP PREDICTIONS")
        pred_map = run_lexecutor(snippet_obj)
        print(pred_map)

    print("ASSOCIATIONS")
    print(tbd_associations)

    # Initialize tally for deductions
    deductions_tally = {'list': 0, 'dict': 0, 'set': 0, 'int': 0, 'str': 0, 'callable': 0, 'object': 0, 'total': 0}
    for_inctp = []
    to_annotate = {}

    final_code_snippet = code_snippet

    if(executability):
        old_stmt_cov, old_br_cov = coverage_report['stmt'], coverage_report['br']

        for class_name, info in unroll_dict.items():
            # Backup the current state before applying the change
            original_code_snippet = code_snippet

            is_preprocessed_tbd = class_name in snippet_obj.preprocessed_tbds
            
            if info['type'] in ['list', 'dict', 'set', 'int', 'str']:
                # Apply one change at a time
                updated_code_snippet = apply_single_replacement(code_snippet, class_name, info, class_container_init)
                success, stmt_cov, br_cov = test_snippet(snippet_obj, updated_code_snippet)

                if success:
                    # If the change is successful, update the code_snippet
                    # print('\nUNMOCKER: SUCCESSFUL SNIPPET:\n{}\n'.format(code_snippet))
                    code_snippet = updated_code_snippet

                    if not is_preprocessed_tbd:
                        deductions_tally[info['type']] += 1
                        deductions_tally['total'] += 1
                else:
                    # If info['type'] is 'list', try now with 'dict'
                    fuzz_success, fuzzed_snippet = fuzz(snippet_obj, code_snippet, class_name, info, class_container_init, unroll_dict)
                    if fuzz_success:
                        code_snippet = fuzzed_snippet
                        if not is_preprocessed_tbd:
                            deductions_tally[info['type']] += 1
                            deductions_tally['total'] += 1
                    else:
                        if Session.lextp:
                            # predict
                            updated_code_snippet, pred_type = cross_check(snippet_obj, pred_map, class_name)
                            
                            if pred_type in ['object']:
                                if Session.inctp:
                                    # reserve for inctp to later predict once everything is deduced/predicted with lextp
                                    for_inctp.append(class_name)
                            else:
                                success, stmt_cov, br_cov = test_snippet(snippet_obj, updated_code_snippet)

                                # check cov
                                if success and stmt_cov >= old_stmt_cov:
                                    if old_br_cov is None or (old_br_cov is not None and br_cov is not None and br_cov > old_br_cov):
                                        code_snippet = updated_code_snippet
                                        old_stmt_cov, old_br_cov = stmt_cov, br_cov

                                        info['type'] = pred_type
                                        info['deductions'].append('predicted by lextp')
                                        if not is_preprocessed_tbd:
                                            deductions_tally[info['type']] += 1
                                else:
                                    # If not successful, revert to original
                                    code_snippet = original_code_snippet

                        if not is_preprocessed_tbd and info['type'] is not None:
                            deductions_tally['total'] += 1
                    
            elif info['type'] in ['object']:
                if Session.lextp:
                    # predict
                    updated_code_snippet, pred_type = cross_check(snippet_obj, pred_map, class_name)

                    if pred_type in ['object']:
                        if Session.inctp:
                            # reserve for inctp to later predict once everything is deduced/predicted with lextp
                            for_inctp.append(class_name)
                    else:
                        success, stmt_cov, br_cov = test_snippet(snippet_obj, updated_code_snippet)

                        # check cov
                        if success and stmt_cov >= old_stmt_cov:
                            if old_br_cov is None or (old_br_cov is not None and br_cov is not None and br_cov > old_br_cov):
                                code_snippet = updated_code_snippet
                                old_stmt_cov, old_br_cov = stmt_cov, br_cov

                                info['type'] = pred_type
                                info['deductions'].append('predicted by lextp')
                                if not is_preprocessed_tbd and info['type'] is not None:
                                    deductions_tally[info['type']] += 1
                        else:
                            # If not successful, revert to original
                            code_snippet = original_code_snippet

                if not is_preprocessed_tbd:
                    deductions_tally['object'] += 1
                continue
            
            elif 'user-defined' in info['deductions']:
                # annotate tbd with info['type']
                to_annotate[class_name] = info['type']

        # remove unreferenced tbd classes
        final_code_snippet = remove_unused_classes(code_snippet)

        # at this point IncTP uses the already unmocked snippet as context and predicts library types for the tbds that have been identified as "object" type by both IncTD and LexTP
        for tbd in for_inctp:
            library_type = query_inctp(final_code_snippet, snippet_obj, tbd)
            print('\nPREDICTED BY INCTP: ({}, {})\n'.format(tbd, library_type))
            
            unroll_dict[tbd]['type'] = library_type
            unroll_dict[tbd]['deductions'].append('predicted by inctp')
            
            # annotate
            to_annotate[tbd] = library_type

        # annotate
        for (tbd, _type) in to_annotate.items():
            final_code_snippet = final_code_snippet.replace(tbd+'()', tbd+'()'+' # {}'.format(_type))

    # Update results file
    res = {}
    if os.path.exists(res_path):
        with open(res_path, 'r') as res_file:
            res_content = res_file.read()
            if len(res_content) > 0:
                res = json.loads(res_content)
    else:
        with open(res_path, 'w+') as res_file:
            json.dump(res, res_file)

    with open(res_path, 'w+') as res_file:
        # Extract the snippet number from the snippet name (e.g., "snippet_748-3.py" -> "748")
        snippet_no = snippet_obj.snippet_name.replace('snippet_', '').split('.')[0]

        for identifier, info in tbd_associations.items():
            if snippet_no in refs.keys():
                if identifier in refs[snippet_no].keys():
                    tbd_name = info['tbd_name'].replace('()', '').strip()  # Remove parentheses for matching

                    if tbd_name in unroll_dict:
                        deduced_type = unroll_dict[tbd_name]['type']

                        if info['type'] == 'callable':
                            deduced_type = "callable"
                        elif deduced_type == "object" and info['type'] == 'object':
                            deduced_type = "object"

                    res[snippet_no] = {identifier: deduced_type}

        json.dump(res, res_file, indent=2)
    
    # print(deductions_tally)
    for var, info in unroll_dict.items():
        print(f"{var}: {info}")
    
    return final_code_snippet, deductions_tally


# To run directly for testing
if __name__ == "__main__":
    code_snippet = """ 
    """
    unroll_dict, class_container_init = analyze_code_to_unroll_dict(code_snippet)
    # updated_code_snippet = apply_replacements_and_remove_classes(code_snippet, unroll_dict, class_container_init)
    for var, info in unroll_dict.items():
        print(f"{var}: {info}")
    # print(updated_code_snippet)