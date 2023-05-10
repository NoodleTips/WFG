
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QLinearGradient
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QLineEdit, QPushButton, QFileDialog, \
    QMessageBox

class WFG(QMainWindow):

    def __init__(self):
        super().__init__()

        self.__init_da_GUI()

    def __init_da_GUI(self):
        # background-color
        self.setStyleSheet("background-color: lightblue;")
        font = QFont("Helvetica", 8, QFont.Bold)
        # rainbow gradient for text
        palette = QPalette()
        gradient = QLinearGradient(0,0,0,20)
        gradient.setColorAt(0.00, Qt.red)
        gradient.setColorAt(0.16, Qt.yellow)
        gradient.setColorAt(0.33, Qt.green)
        gradient.setColorAt(0.50, Qt.cyan)
        gradient.setColorAt(0.66, Qt.blue)
        gradient.setColorAt(0.83, Qt.magenta)
        gradient.setColorAt(1.00, Qt.red)
        palette.setBrush(QPalette.WindowText, gradient)

        # ###############################/\
        # label for allowed IP's
        self.ip_label = QLabel("Allowed IP Address:  ", self)
        self.ip_label.move(50,50)
        self.ip_label.setWordWrap(True)
        self.ip_label.setStyleSheet('color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #FF0000, stop:0.16 #FF7F00, stop:0.33 #FFFF00, stop:0.5 #00FF00, stop:0.66 #00FFFF, stop:0.83 #0000FF, stop:1 #FF00FF);')
        self.ip_label.setFont(font)

        # text input for allowed IP's
        self.ip_input = QLineEdit(self)
        self.ip_input.move(150,50)
        # ###############################\/

        # ###############################/\
        # label for allowed port's
        self.port_label = QLabel("Allowed Port:",self)
        self.port_label.move(50,100)
        self.port_label.setStyleSheet('color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #FF0000, stop:0.16 #FF7F00, stop:0.33 #FFFF00, stop:0.5 #00FF00, stop:0.66 #00FFFF, stop:0.83 #0000FF, stop:1 #FF00FF);')
        self.port_label.setFont(font)

        # dropdown list for allowed ports
        self.port_combo = QComboBox(self)
        self.port_combo.addItem("21")   #FTP
        self.port_combo.addItem("22")   #SSH
        self.port_combo.addItem("23")   #Telnet
        self.port_combo.addItem("25")   #SMTP
        self.port_combo.addItem("49")   #TACACS
        self.port_combo.addItem("53")   #DNS
        self.port_combo.addItem("67")   #DHCP (UDP - Server)
        self.port_combo.addItem("68")   #DHCP (UDP - Client)
        self.port_combo.addItem("69")   #TFTP (UDP)
        self.port_combo.addItem("80")   #HTTP
        self.port_combo.addItem("88")   #Kerberos
        self.port_combo.addItem("110")  #POP3
        self.port_combo.addItem("111")  #RPC
        self.port_combo.addItem("123")  #NTP (UDP)
        self.port_combo.addItem("135")  #Windows RPC
        self.port_combo.addItem("137")  #NetBIOS
        self.port_combo.addItem("138")  #NetBIOS
        self.port_combo.addItem("139")  #SMB
        self.port_combo.addItem("143")  #IMAP
        self.port_combo.addItem("161")  #SNMP (UDP)
        self.port_combo.addItem("179")  #BGP
        self.port_combo.addItem("389")  #LDAP
        self.port_combo.addItem("443")  #HTTPS
        self.port_combo.addItem("445")  #SMB
        self.port_combo.addItem("500")  #ISAKMP (UDP)
        self.port_combo.addItem("514")  #Syslog
        self.port_combo.addItem("520")  #RIP
        self.port_combo.addItem("546")  #DHCPv6
        self.port_combo.addItem("547")  #DHCPv6
        self.port_combo.addItem("587")  #SMTP
        self.port_combo.addItem("902")  #VMWare
        self.port_combo.addItem("1080") #Socks Proxy
        self.port_combo.addItem("1194") #VPN
        self.port_combo.addItem("1433") #MS-SQL
        self.port_combo.addItem("1434") #Oracle
        self.port_combo.addItem("1521") #DameWare
        self.port_combo.addItem("1629") #NFS
        self.port_combo.addItem("2049") #Squid Proxy
        self.port_combo.addItem("3128") #MySQL
        self.port_combo.addItem("3306") #RDP
        self.port_combo.addItem("3389") #SIP
        self.port_combo.addItem("5060") #Jabber
        self.port_combo.addItem("5222") #Postgres
        self.port_combo.addItem("5432") #Nagios
        self.port_combo.addItem("5666") #VNC
        self.port_combo.addItem("5900") #X11
        self.port_combo.addItem("6000") #DameWare
        self.port_combo.addItem("6129") #IRC
        self.port_combo.addItem("6667") #TOR
        self.port_combo.addItem("9001") #HSQL
        self.port_combo.addItem("9090") #Openfire
        self.port_combo.addItem("9091") #Openfire
        self.port_combo.addItem("9100") #Jet Direct (HP)
        self.port_combo.move(150,100)
        # ###############################\/

        # ###############################/\
        # label for generate button
        self.gen_push_button_label = QLabel("1: Click to generate.", self)
        self.gen_push_button_label.move(50,300)
        self.gen_push_button_label.setWordWrap(True)
        self.gen_push_button_label.setStyleSheet('color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #FF0000, stop:0.16 #FF7F00, stop:0.33 #FFFF00, stop:0.5 #00FF00, stop:0.66 #00FFFF, stop:0.83 #0000FF, stop:1 #FF00FF);')
        self.gen_push_button_label.setFont(font)


        # generate button
        self.gen_push_button = QPushButton("Generate Rule", self)
        self.gen_push_button.move(150,300)
        self.gen_push_button.clicked.connect(self.generate_da_rule)
        self.gen_push_button.setFont(font)
        # ###############################\/

        # ###############################/\
        # label for save button
        self.browse_button_label = QLabel("2: Click to save.", self)
        self.browse_button_label.move(50,350)
        self.browse_button_label.setWordWrap(True)
        self.browse_button_label.setStyleSheet('color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #FF0000, stop:0.16 #FF7F00, stop:0.33 #FFFF00, stop:0.5 #00FF00, stop:0.66 #00FFFF, stop:0.83 #0000FF, stop:1 #FF00FF);')
        self.browse_button_label.setFont(font)
        # save button
        self.browse_button = QPushButton('Save to', self)
        self.browse_button.move(150,350)
        self.browse_button.clicked.connect(self.browse_file)
        self.browse_button.setFont(font)
        # ###############################\/

        # window size/title
        self.setGeometry(100,100,400,450)
        self.setWindowTitle('WFG - Windows Firewall(rule) Generator')
        self.show()

    def generate_da_rule(self):
        # gets text input from gui
        ip_address = self.ip_input.text()
        port = self.port_combo.currentText()
        # building firewall rule in string format
        rule = 'netsh advfirewall firewall add rule name="Allow {0} on port {1}" protocol=TCP dir=in localport={1} remoteip={0}'.format(ip_address, port)
        # save it
        self.save_rule(rule)

    def browse_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self,'Save Rule','','Text Files (*.txt);;All Files (*.*)')
        if file_path:
            with open(file_path, 'a') as f:
                f.write(self.rule + '\n')
                self.show_message('Rule Created!')

    def save_rule(self, rule):
        self.rule = rule

    # save confirmation message
    def show_message(self,message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Rule saved successfully.')
        msg.setInformativeText(message)
        msg.setWindowTitle('Info')
        msg.exec_()



if __name__ == '__main__':              # if executed directly. if not, no worky :(
    app = QApplication(sys.argv)        # allows command-line args for PyQt
    wfg = WFG()                         # creates instance
    sys.exit(app.exec_())               # starts event loop /terminates with an eventual exit code














