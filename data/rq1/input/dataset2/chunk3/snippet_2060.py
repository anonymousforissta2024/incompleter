#Source: https://stackoverflow.com/questions/56961816/attributeerror-list-object-has-no-attribute-iter
import xml.etree.ElementTree as et
class SerializerFactory:

    def serialize_all(self, format, member_list):
        if format == 'JSON':
            serialize = JsonSerializer(member_list)
            serialize.start_all_objects()
            return serialize
        elif format == 'XML':
            serialize = XmlSerializer(member_list)
            serialize.start_all_objects()
            return serialize
        else:
            raise ValueError("Format must be 'JSON' or 'XML'.")

    def serialize_one(self, format, index, member_list):
        if format == 'JSON':
            return JsonSerializer(member_list).start_one_object(index)
        elif format == 'XML':
            return XmlSerializer(member_list).start_one_object(index)
        else:
            raise ValueError("Format must be 'JSON' or 'XML'.")


class XmlSerializer:
    def __init__(self, member_list):
        self.member_list = member_list
        self.serialize_list = [] * member_list.size

    def start_all_objects(self):
        for i in range(self.member_list.size):
            member = self.member_list[i]
            number = member.mem_num
            l_name = member.l_name
            f_name = member.f_name
            mem_type = member.mem_type
            mem_list = et.Element({'Number': number, 'Last Name': l_name,
                                   'First Name': f_name, 'Membership Type': mem_type})

            self.serialize_list.append(mem_list)

    def start_one_object(self, index):
        member = self.member_list[index]
        number = member.mem_num
        l_name = member.l_name
        f_name = member.f_name
        mem_type = member.mem_type
        mem_list = et.Element({'Number': number, 'Last Name': l_name,
                               'First Name': f_name, 'Membership Type': mem_type})
        self.serialize_list.append(mem_list)

    def to_str(self):
        return et.tostring(self.serialize_list, encoding='unicode')


factory = MemberSerializer.SerializerFactory()
xml = factory.serialize_all('XML', mem_list)
print(xml.to_str())