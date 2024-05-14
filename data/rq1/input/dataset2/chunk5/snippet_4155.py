#Source: https://stackoverflow.com/questions/61943976/how-to-pass-element-tree-to-other-function-typeerror-elementtree-object-is-no
class TestXMl(http.Controller):
    @http.route('/xml/download/report', type='http', auth="user")
    @serialize_exception
    def sale_xml_download(self, model, id, filename=None, **kw):
        filename = 'Test%s.xml'%('Test')
        records= http.request.env['sale.order'].search([('some_attribute', '=', True)])
        if records:
            xml_record = http.request.env['sale.order']._xml_download()
        else:
            xml_record = 'Test'
        filename = 'Test%s.xml'%('Test')

        headers = [
                ('Content-Type', 'application/xml'),
                ('Content-Disposition', content_disposition(filename)),
                ('charset', 'utf-8'),
            ]
        return request.make_response(
                    xml_record, headers=headers, cookies=None)