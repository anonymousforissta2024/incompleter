#Source: https://stackoverflow.com/questions/74698367/nameerror-name-lemma-from-key-is-not-defined
class _WordNetObject:

    def lemma(self, name, lang="eng"):
        """Return lemma object that matches the name"""
        # cannot simply split on first '.',
        # e.g.: '.45_caliber.a.01..45_caliber'
        separator = SENSENUM_RE.search(name).end()

        synset_name, lemma_name = name[: separator - 1], name[separator:]

        synset = self.synset(synset_name)
        for lemma in synset.lemmas(lang):
            if lemma._name == lemma_name:
                return lemma
        raise WordNetError(f"no lemma {lemma_name!r} in {synset_name!r}")

    def lemma_from_key(self, key):
        # Keys are case sensitive and always lower-case
        key = key.lower()

        lemma_name, lex_sense = key.split("%")
        pos_number, lexname_index, lex_id, _, _ = lex_sense.split(":")
        pos = self._pos_names[int(pos_number)]

        # open the key -> synset file if necessary
        if self._key_synset_file is None:
            self._key_synset_file = self.open("index.sense")

        # Find the synset for the lemma.
        synset_line = _binary_search_file(self._key_synset_file, key)
        if not synset_line:
            raise WordNetError("No synset found for key %r" % key)
        offset = int(synset_line.split()[1])
        synset = self.synset_from_pos_and_offset(pos, offset)
        # return the corresponding lemma
        for lemma in synset._lemmas:
            if lemma._key == key:
                return lemma
        raise WordNetError("No lemma found for for key %r" % key)

    #############################################################
    # Loading Synsets
    #############################################################
    def synset(self, name):
        # split name into lemma, part of speech and synset number
        lemma, pos, synset_index_str = name.lower().rsplit(".", 2)
        synset_index = int(synset_index_str) - 1

        # get the offset for this synset
        try:
            offset = self._lemma_pos_offset_map[lemma][pos][synset_index]
        except KeyError as e:
            message = "no lemma %r with part of speech %r"
            raise WordNetError(message % (lemma, pos)) from e
        except IndexError as e:
            n_senses = len(self._lemma_pos_offset_map[lemma][pos])
            message = "lemma %r with part of speech %r has only %i %s"
            if n_senses == 1:
                tup = lemma, pos, n_senses, "sense"
            else:
                tup = lemma, pos, n_senses, "senses"
            raise WordNetError(message % tup) from e

        # load synset information from the appropriate file
        synset = self.synset_from_pos_and_offset(pos, offset)

        # some basic sanity checks on loaded attributes
        if pos == "s" and synset._pos == "a":
            message = (
                "adjective satellite requested but only plain "
                "adjective found for lemma %r"
            )
            raise WordNetError(message % lemma)
        assert synset._pos == pos or (pos == "a" and synset._pos == "s")

        # Return the synset object.
        return synset

    def _data_file(self, pos):
        """
        Return an open file pointer for the data file for the given
        part of speech.
        """
        if pos == ADJ_SAT:
            pos = ADJ
        if self._data_file_map.get(pos) is None:
            fileid = "data.%s" % self._FILEMAP[pos]
            self._data_file_map[pos] = self.open(fileid)
        return self._data_file_map[pos]

    def synset_from_pos_and_offset(self, pos, offset):
        """
        - pos: The synset's part of speech, matching one of the module level
          attributes ADJ, ADJ_SAT, ADV, NOUN or VERB ('a', 's', 'r', 'n', or 'v').
        - offset: The byte offset of this synset in the WordNet dict file
          for this pos.

        >>> from nltk.corpus import wordnet as wn
        >>> print(wn.synset_from_pos_and_offset('n', 1740))
        Synset('entity.n.01')
        """
        # Check to see if the synset is in the cache
        if offset in self._synset_offset_cache[pos]:
            return self._synset_offset_cache[pos][offset]

        data_file = self._data_file(pos)
        data_file.seek(offset)
        data_file_line = data_file.readline()
        # If valid, the offset equals the 8-digit 0-padded integer found at the start of the line:
        line_offset = data_file_line[:8]
        if line_offset.isalnum() and offset == int(line_offset):
            synset = self._synset_from_pos_and_line(pos, data_file_line)
            assert synset._offset == offset
            self._synset_offset_cache[pos][offset] = synset
        else:
            synset = None
            raise WordNetError(
                f"No WordNet synset found for pos={pos} at offset={offset}."
            )
        data_file.seek(0)
        return synset

    @deprecated("Use public method synset_from_pos_and_offset() instead")
    def _synset_from_pos_and_offset(self, *args, **kwargs):
        """
        Hack to help people like the readers of
        https://stackoverflow.com/a/27145655/1709587
        who were using this function before it was officially a public method
        """
        return self.synset_from_pos_and_offset(*args, **kwargs)

    def _synset_from_pos_and_line(self, pos, data_file_line):
        # Construct a new (empty) synset.
        synset = Synset(self)

        # parse the entry for this synset
        try:

            # parse out the definitions and examples from the gloss
            columns_str, gloss = data_file_line.strip().split("|")
            definition = re.sub(r"[\"].*?[\"]", "", gloss).strip()
            examples = re.findall(r'"([^"]*)"', gloss)
            for example in examples:
                synset._examples.append(example)

            synset._definition = definition.strip("; ")

            # split the other info into fields
            _iter = iter(columns_str.split())

            def _next_token():
                return next(_iter)

            # get the offset
            synset._offset = int(_next_token())

            # determine the lexicographer file name
            lexname_index = int(_next_token())
            synset._lexname = self._lexnames[lexname_index]

            # get the part of speech
            synset._pos = _next_token()

            # create Lemma objects for each lemma
            n_lemmas = int(_next_token(), 16)
            for _ in range(n_lemmas):
                # get the lemma name
                lemma_name = _next_token()
                # get the lex_id (used for sense_keys)
                lex_id = int(_next_token(), 16)
                # If the lemma has a syntactic marker, extract it.
                m = re.match(r"(.*?)(\(.*\))?$", lemma_name)
                lemma_name, syn_mark = m.groups()
                # create the lemma object
                lemma = Lemma(self, synset, lemma_name, lexname_index, lex_id, syn_mark)
                synset._lemmas.append(lemma)
                synset._lemma_names.append(lemma._name)

            # collect the pointer tuples
            n_pointers = int(_next_token())
            for _ in range(n_pointers):
                symbol = _next_token()
                offset = int(_next_token())
                pos = _next_token()
                lemma_ids_str = _next_token()
                if lemma_ids_str == "0000":
                    synset._pointers[symbol].add((pos, offset))
                else:
                    source_index = int(lemma_ids_str[:2], 16) - 1
                    target_index = int(lemma_ids_str[2:], 16) - 1
                    source_lemma_name = synset._lemmas[source_index]._name
                    lemma_pointers = synset._lemma_pointers
                    tups = lemma_pointers[source_lemma_name, symbol]
                    tups.append((pos, offset, target_index))

            # read the verb frames
            try:
                frame_count = int(_next_token())
            except StopIteration:
                pass
            else:
                for _ in range(frame_count):
                    # read the plus sign
                    plus = _next_token()
                    assert plus == "+"
                    # read the frame and lemma number
                    frame_number = int(_next_token())
                    frame_string_fmt = VERB_FRAME_STRINGS[frame_number]
                    lemma_number = int(_next_token(), 16)
                    # lemma number of 00 means all words in the synset
                    if lemma_number == 0:
                        synset._frame_ids.append(frame_number)
                        for lemma in synset._lemmas:
                            lemma._frame_ids.append(frame_number)
                            lemma._frame_strings.append(frame_string_fmt % lemma._name)
                    # only a specific word in the synset
                    else:
                        lemma = synset._lemmas[lemma_number - 1]
                        lemma._frame_ids.append(frame_number)
                        lemma._frame_strings.append(frame_string_fmt % lemma._name)

        # raise a more informative error with line text
        except ValueError as e:
            raise WordNetError(f"line {data_file_line!r}: {e}") from e

        # set sense keys for Lemma objects - note that this has to be
        # done afterwards so that the relations are available
        for lemma in synset._lemmas:
            if synset._pos == ADJ_SAT:
                head_lemma = synset.similar_tos()[0]._lemmas[0]
                head_name = head_lemma._name
                head_id = "%02d" % head_lemma._lex_id
            else:
                head_name = head_id = ""
            tup = (
                lemma._name,
                WordNetCorpusReader._pos_numbers[synset._pos],
                lemma._lexname_index,
                lemma._lex_id,
                head_name,
                head_id,
            )
            lemma._key = ("%s%%%d:%02d:%02d:%s:%s" % tup).lower()

        # the canonical name is based on the first lemma
        lemma_name = synset._lemmas[0]._name.lower()
        offsets = self._lemma_pos_offset_map[lemma_name][synset._pos]
        sense_index = offsets.index(synset._offset)
        tup = lemma_name, synset._pos, sense_index + 1
        synset._name = "%s.%s.%02i" % tup

        return synset

    def synset_from_sense_key(self, sense_key):
        """
        Retrieves synset based on a given sense_key. Sense keys can be
        obtained from lemma.key()

        From https://wordnet.princeton.edu/documentation/senseidx5wn:
        A sense_key is represented as::

            lemma % lex_sense (e.g. 'dog%1:18:01::')

        where lex_sense is encoded as::

            ss_type:lex_filenum:lex_id:head_word:head_id

        :lemma:       ASCII text of word/collocation, in lower case
        :ss_type:     synset type for the sense (1 digit int)
                      The synset type is encoded as follows::

                          1    NOUN
                          2    VERB
                          3    ADJECTIVE
                          4    ADVERB
                          5    ADJECTIVE SATELLITE
        :lex_filenum: name of lexicographer file containing the synset for the sense (2 digit int)
        :lex_id:      when paired with lemma, uniquely identifies a sense in the lexicographer file (2 digit int)
        :head_word:   lemma of the first word in satellite's head synset
                      Only used if sense is in an adjective satellite synset
        :head_id:     uniquely identifies sense in a lexicographer file when paired with head_word
                      Only used if head_word is present (2 digit int)

        >>> import nltk
        >>> from nltk.corpus import wordnet as wn
        >>> print(wn.synset_from_sense_key("drive%1:04:03::"))
        Synset('drive.n.06')

        >>> print(wn.synset_from_sense_key("driving%1:04:03::"))
        Synset('drive.n.06')
        """
        return self.lemma_from_key(sense_key).synset()#line 1680