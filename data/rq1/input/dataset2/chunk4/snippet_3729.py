#Source: https://stackoverflow.com/questions/53162259/populating-word-template-with-python-merge-but-typeerror-merge-argument-af
stress_notes_document = MailMerge(os.path.join(new_path,new_notes))
stress_notes_document.merge(
        TR_num = packet_info['TR#'],
        pckg_num = packet_info['Package#'],
        TED_num = packet_info['TED#'],
        Charge_Line = packet_info['Charge Line'],
        Change_num = packet_info['Change#'],
        Installation_list  = packet_list['Installations list'],
        Drawings_list   = packet_list['Drawings list'],
        Designer  = packet_info['Designer'],
        phone_number_designer = packet_info['Phone Number of designer'],
        Date_in = packet_info['Date in'],
        Stress_Due_Date = packet_info['Stress Due Date'],
        Date_out = packet_info['Date out'],
        model = packet_info['model'],
        Customer = packet_info['Customer'],
        Effectivity  = packet_info['Effectivity'],
        panel_excel = 'new_panel')

stress_notes_document.write(os.path.join(new_path,new_notes + "ver A"))