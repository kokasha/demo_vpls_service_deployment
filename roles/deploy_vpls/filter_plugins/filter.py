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
            'jnpr_get_vpls_circuits': self.jnpr_get_vpls_circuits
            # 'filter_pyats_ios_pfx_list': self.filter_pyats_ios_pfx_list
        }
    def jnpr_get_vpls_circuits(self,vpls_output):
        result = {}

        if isinstance(vpls_output,dict):
            instance_name = vpls_output['name']
            links = vpls_output['interface']['name']
            result[instance_name] = {'links':links}
            return result

        if isinstance(vpls_output,list):
            for instance in vpls_output:
                instance_name = instance['name']
                links = instance['interface']['name']
                result[instance_name] = {'links':links}
            return result


    @staticmethod
    def _get_links(vpls_intfs):
        
        if isinstance(vpls_intfs,list):
            all_links = [ l['interface-name'] for l in vpls_intfs if 'ge' in l['interface-name'] ]
            return { 'links': all_links }

        elif isinstance(vpls_intfs,dict):
            return { 'links': [ vpls_intfs['interface-name'] ] }

        else:
            return {'links':''}

    def jnpr_parse_vpls_connections(self, vpls_output):

        vpls_data = vpls_output['rpc-reply']['vpls-connection-information']['instance']
        
        vpls_circuits = {}

        if isinstance(vpls_data,dict):

            vpls_name = vpls_data['instance-name']
            vpls_links_dict = self._get_links(vpls_data['reference-site']['interface'])
            vpls_circuits[vpls_name] = vpls_links_dict

            print(json.dumps(vpls_circuits))

            return vpls_circuits

        if isinstance(vpls_data,list):

            for vpls_crkt in vpls_data:
                vpls_name = vpls_crkt['instance-name']
                vpls_links_dict = self._get_links(vpls_crkt['reference-site']['interface'])
                vpls_circuits[vpls_name] = vpls_links_dict

            print(json.dumps(vpls_circuits))

            return vpls_circuits

    # @staticmethod        
    # def vpls_diff(vpls_int_state,vpls_current_state):
        
    #     cleanup_data = dict()
    #     provision_data = dict()
    #     for vpls_instance in vpls_int_state:
    #         vpls_crkts = 
