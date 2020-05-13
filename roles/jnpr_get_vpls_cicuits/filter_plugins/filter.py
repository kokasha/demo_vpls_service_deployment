import json


# class VplsCircuit(object):
#     def __init__(self,instance,intfs=[]):
#         self.instance = instance
#         self.intfs = intfs

#     def __repr__(self):
#         return f'VPLS instance {self.instance} on {",".join(self.intfs)}'
    
#     def __eq__(self,other):
#         if (self.instance == other.instance) and \
#             sorted(self.intfs) == sorted(other.intfs):
#             return True
#         else:
#             return False


# x = VplsCircuit(instance='vpls01',intfs=['ge-0/0/0','ge-0/0/1'])
# y = VplsCircuit(instance='vpls01',intfs=['ge-0/0/1','ge-0/0/0'])
# print(x)

# print(x==y)

# print(sorted(['ge-0/0/20','ge-0/0/1']))

# from ipaddress import IPv4Network

class FilterModule(object):
    def filters(self):
        return {
            'jnpr_parse_vpls_connections': self.jnpr_parse_vpls_connections
            # 'filter_pyats_ios_pfx_list': self.filter_pyats_ios_pfx_list
        }

    @staticmethod
    def _get_links(vpls_intfs):
        
        if isinstance(vpls_intfs,list):
            all_links = [ l['interface-name'] for l in vpls_intfs if l['interface-name'].startwith('ge-')]
            return { 'links': all_links }

        elif isinstance(vpls_intfs,dict):
            return { 'links': vpls_intfs['interface-name'] }

        else:
            return {'links':''}

    def jnpr_parse_vpls_connections(self, vpls_output):

        vpls_data = vpls_output['rpc-reply']['vpls-connection-information']['instance']
        
        vpls_circuits = {}

        if isinstance(vpls_data,dict):

            return {}
            # vpls_name = vpls_data['instance_name']
            # vpls_links_dict = self._get_links(vpls_data['reference-site']['interface'])
            # vpls_circuits[vpls_name] = vpls_links_dict

            # print(json.dumps(vpls_circuits))

            # return vpls_circuits

        if isinstance(vpls_data,list):

            return {}
            # for vpls_crkt in vpls_data:
            #     vpls_name = vpls_crkt['instance_name']
            #     vpls_links_dict = self._get_links(vpls_crkt['reference-site']['interface'])
            #     vpls_circuits[vpls_name] = vpls_links_dict

            # print(json.dumps(vpls_circuits))

            # return vpls_circuits
            
