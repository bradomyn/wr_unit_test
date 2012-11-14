import socket
import wr_log


class net:
    def __init__(self, net_cfg):
        self.net_type = net_type;   # client or server


    def create_socket(self)

        # socket creation
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, \
                             socket.IPPROTO_UDP)
        except:
            wr_log.log.exception("Creating socket")
            return 0
        
        # binding the socket
        if self.net_cfg.server:
            try:
                #self.sock.bind(self.net_cfg.server_ip,self.net_cfg.server_port)
                sock.bind(socket.gethostbyname(socket.gethostname()),1501)
            except:            
                wr_log.log.exception("Binding socket in server")
                return 0
        elif self.net_cfg.client:
             try:
                #self.sock.bind(self.net_cfg.server_ip,self.net_cfg.server_port)
                sock.bind(socket.gethostbyname(socket.gethostname()),1501)
            except:            
                wr_log.log.exception("Binding socket in server")
                return 0
            

        if self.net_cfg.multicast:
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
         


            


           




 
