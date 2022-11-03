"""
PCON Software (Power CONtroller Software)

"""
import socket

# These items will need to be placed into a data base eventually.
# Creating a data structure just to understand the basic 
# power
CORE_ELECTRIC_Resendential = {
    'basic_service_charge' : 13.50,
    'energy_charge'        : 0.11627,
    'peak_usage_times'     : [(1600, 2000)],
    'demand_charge'        : 2.00
}
#source: https://core.coop/my-cooperative/rates-and-regulations/rate-schedules/

CORE_ELECTRIC_NonResendential = {}

Colorado_Sprints_E1R = {
    'access_charge_per_day' : 0.5103,
    'access_charge_per_kWh' : 0.0777,

}

Colorado_Sprints_ETR = {
    'on_peak_access_facilities_charge': 0.1827,
    'off_peak_access_facilities_charge': 0.0522,
}

def pcon_client_program(port=5000):
    host = socket.gethostname()  # as both code is running on same pcr

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

class pcon_cli_application():
    """ """
    def __init__(self, utility_company_description):
        self.basic_service_charge = utility_company_description['basic_service_charge']
        self.energy_charge        = utility_company_description['energy_charge']
        self.peak_usage_times     = utility_company_description['peak_usage_times']
        self.client_connection = pcon_client_program(5500)
        
def banner(text, ch='-', length=78):
    """ """
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    return banner


def main():
    """ """
    print(banner("Welcom to Pcon"))
    pcon = pcon_cli_application(CORE_ELECTRIC_Resendential)
    print(pcon.basic_service_charge)
    
   
    
if __name__ == "__main__":
    main()
