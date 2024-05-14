#Source: https://stackoverflow.com/questions/45944787/attributeerror-across-typeerror-issue-in-python-3-2
def write_cbs_from_poll_response_11(self, poll_response, dest_dir, write_type_=W_CLOBBER):

    for cb in poll_response.content_blocks:
        if cb.content_binding.binding_id == CB_STIX_XML_10:
            format_ = '_STIX10_'
            ext = '.xml'
        elif cb.content_binding.binding_id == CB_STIX_XML_101:
            format_ = '_STIX101_'
            ext = '.xml'
        elif cb.content_binding.binding_id == CB_STIX_XML_11:
            format_ = '_STIX11_'
            ext = '.xml'
        elif cb.content_binding.binding_id == CB_STIX_XML_111:
            format_ = '_STIX111_'
            ext = '.xml'
        elif cb.content_binding.binding_id == CB_STIX_XML_12:
            format_ = '_STIX12_'
            ext = '.xml'
        else:  # Format and extension are unknown
            format_ = ''
            ext = ''

        if cb.timestamp_label:
            date_string = 't' + cb.timestamp_label.isoformat()
        else:
            date_string = 's' + datetime.datetime.now().isoformat()

        filename = gen_filename(poll_response.collection_name,
                                format_,
                                date_string,
                                ext)
        filename = os.path.join(dest_dir, filename)
        write, message = TaxiiScript.get_write_and_message(filename, write_type_)

        if write:
            with open(filename, 'w') as f:
                f.write(cb.content)           # The TypeError is thrown here

        print("%s%s" % (message, filename))