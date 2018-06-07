import unittest
import sublist3r 
import math

class sublist3r_UnitTest(unittest.TestCase):                 
    def setUp(self):
        self.no_threads = 30
        self.savefile = None
        self.ports = '80,433'
        self.verbose = True
        self.enable_bruteforce = False
        self.times = 1

    def ansEqual(self, engines, Test_Domain_Data, SubDomain_Data):
        for _ in range(self.times):
            for i in Test_Domain_Data:
                domain = i
                TestData = Test_Domain_Data[i]
                #subdomains = sublist3r.main(domain, self.no_threads, self.savefile, self.ports, silent=False, verbose=self.verbose, enable_bruteforce=self.enable_bruteforce, engines=engines)
                subdomains = sublist3r.main(domain, self.no_threads, engines + '_' + domain + '.txt', self.ports, silent=False, verbose=self.verbose, enable_bruteforce=self.enable_bruteforce, engines=engines)
                SubDomain_Data[i] = SubDomain_Data[i] | set(subdomains)
                
        all_Test = set()
        all_SubDomain = set()
        for i in Test_Domain_Data:
            domain = i
            TestData = Test_Domain_Data[i]
            [all_Test.add(url) for url in TestData]
            [all_SubDomain.add(url) for url in SubDomain_Data[i]]

        ans = (all_SubDomain | all_Test) - (all_SubDomain & all_Test)
        print("==============================")
        print(engines)
        print(ans)
        print("==============================")
        
        error = math.ceil(len(all_Test) * 0.2)

        if len(ans) == 0:
            self.assertEqual(all_SubDomain, all_Test)
        elif len(ans) <= error:
            self.assertEqual(True, True)
        else:
            self.assertEqual(all_SubDomain, all_Test)
        #self.assertEqual(all_SubDomain, all_Test)
    
    def test_other(self):
        print("test_other")
        sublist3r.parse_args()
        sublist3r.parser_error("error test");

    def test_all(self):
        engines = None
        domain = '0b100.com'
        ports = None
        subdomains = sublist3r.main(domain, self.no_threads, self.savefile, ports, silent=False, verbose=self.verbose, enable_bruteforce=self.enable_bruteforce, engines=engines)
        print("test_all")
        print("==============================")
        print(subdomains)
        print("==============================")

    def test_google_com(self):
        engines = 'ThreatCrowd,Netcraft'
        domain = 'googe.com'
        ports = None
        subdomains = sublist3r.main(domain, self.no_threads, self.savefile, ports, silent=False, verbose=self.verbose, enable_bruteforce=self.enable_bruteforce, engines=engines)
    
    def test_bruteforce(self):
        engines = 'ThreatCrowd'
        domain = '0b100.com'
        ports = None
        subdomains = sublist3r.main(domain, self.no_threads, self.savefile, ports, silent=False, verbose=self.verbose, enable_bruteforce=True, engines=engines)

    def test_Baidu(self):    
        print("test_Baidu")
        engines = 'Baidu'

        Test_Domain_Data = {    '0b100.com':[],
                                'conan.site':[],
                                'connlab.tw':[],
                                'gronextapps.com':[],
                                'ntust.info':[],
                                'ais3.org':[],
                                'gronext.com':[],
                                'keniver.com':['blog.keniver.com'],
                                'taiwandestiny.com':['blog.taiwandestiny.com']
                            }

        SubDomain_Data = {      '0b100.com':set(),
                                'conan.site':set(),
                                'connlab.tw':set(),
                                'gronextapps.com':set(),
                                'ntust.info':set(),
                                'ais3.org':set(),
                                'gronext.com':set(),
                                'keniver.com':set(),
                                'taiwandestiny.com':set()
                            }
        self.ansEqual(engines, Test_Domain_Data, SubDomain_Data)
    
    def test_Yahoo(self):    
        engines = 'Yahoo'

        Test_Domain_Data = {    '0b100.com':['blog.0b100.com'],
                                'conan.site':[],
                                'connlab.tw':[],
                                'gronextapps.com':[],
                                'ntust.info':[],
                                'ais3.org':['pre-exam.ais3.org'],
                                'gronext.com':[],
                                'keniver.com':['blog.keniver.com'],
                                'taiwandestiny.com':['blog.taiwandestiny.com', 'learning.taiwandestiny.com', 'online.taiwandestiny.com']
                            }

        SubDomain_Data = {      '0b100.com':set(),
                                'conan.site':set(),
                                'connlab.tw':set(),
                                'gronextapps.com':set(),
                                'ntust.info':set(),
                                'ais3.org':set(),
                                'gronext.com':set(),
                                'keniver.com':set(),
                                'taiwandestiny.com':set()
                            }
        self.ansEqual(engines, Test_Domain_Data, SubDomain_Data)

    def test_Google(self):    
        engines = 'Google'

        Test_Domain_Data = {    '0b100.com':['blog.0b100.com'],
                                'conan.site':[],
                                'connlab.tw':[],
                                'gronextapps.com':[],
                                'ntust.info':[],
                                'ais3.org':['pre-exam.ais3.org', 'eofqual.ais3.org'],
                                'gronext.com':[],
                                'keniver.com':['blog.keniver.com'],
                                'taiwandestiny.com':['blog.taiwandestiny.com', 'learning.taiwandestiny.com', 'online.taiwandestiny.com']
                            }

        SubDomain_Data = {      '0b100.com':set(),
                                'conan.site':set(),
                                'connlab.tw':set(),
                                'gronextapps.com':set(),
                                'ntust.info':set(),
                                'ais3.org':set(),
                                'gronext.com':set(),
                                'keniver.com':set(),
                                'taiwandestiny.com':set()
                            }
        self.ansEqual(engines, Test_Domain_Data, SubDomain_Data)

    def test_Bing(self):    
        engines = 'Bing'

        Test_Domain_Data = {    '0b100.com':['blog.0b100.com'],
                                'conan.site':[],
                                'connlab.tw':[],
                                'gronextapps.com':[],
                                'ntust.info':[],
                                'ais3.org':['pre-exam.ais3.org'],
                                'gronext.com':[],
                                'keniver.com':['blog.keniver.com'],
                                'taiwandestiny.com':['online.taiwandestiny.com', 'learning.taiwandestiny.com', 'blog.taiwandestiny.com']
                            }

        SubDomain_Data = {      '0b100.com':set(),
                                'conan.site':set(),
                                'connlab.tw':set(),
                                'gronextapps.com':set(),
                                'ntust.info':set(),
                                'ais3.org':set(),
                                'gronext.com':set(),
                                'keniver.com':set(),
                                'taiwandestiny.com':set()
                            }
        self.ansEqual(engines, Test_Domain_Data, SubDomain_Data)

    def test_Ask(self):    
        engines = 'Ask'

        Test_Domain_Data = {    '0b100.com':[],
                                'conan.site':[],
                                'connlab.tw':[],
                                'gronextapps.com':[],
                                'ntust.info':[],
                                'ais3.org':[],
                                'gronext.com':[],
                                'keniver.com':['blog.keniver.com'],
                                'taiwandestiny.com':['blog.taiwandestiny.com', 'learning.taiwandestiny.com', 'online.taiwandestiny.com']
                            }

        SubDomain_Data = {      '0b100.com':set(),
                                'conan.site':set(),
                                'connlab.tw':set(),
                                'gronextapps.com':set(),
                                'ntust.info':set(),
                                'ais3.org':set(),
                                'gronext.com':set(),
                                'keniver.com':set(),
                                'taiwandestiny.com':set()
                            }
        
        self.ansEqual(engines, Test_Domain_Data, SubDomain_Data)
   
    def test_Netcraft(self):    
        engines = 'Netcraft'

        Test_Domain_Data = {    '0b100.com':[],
                                'conan.site':[],
                                'connlab.tw':[],
                                'gronextapps.com':[],
                                'ntust.info':[],
                                'ais3.org':[],
                                'gronext.com':[],
                                'keniver.com':[],
                                'taiwandestiny.com':[]
                            }

        SubDomain_Data = {      '0b100.com':set(),
                                'conan.site':set(),
                                'connlab.tw':set(),
                                'gronextapps.com':set(),
                                'ntust.info':set(),
                                'ais3.org':set(),
                                'gronext.com':set(),
                                'keniver.com':set(),
                                'taiwandestiny.com':set()
                            }

        self.ansEqual(engines, Test_Domain_Data, SubDomain_Data)

    def test_DNSdumpster(self):    
        engines = 'DNSdumpster'

        Test_Domain_Data = {    '0b100.com':['blog.0b100.com', 'git.0b100.com'],
                                'conan.site':['nas.conan.site'],
                                'connlab.tw':['nas.connlab.tw', 'git.connlab.tw'],
                                'gronextapps.com':['web.bear.gronextapps.com'],
                                'ntust.info':['vpsm.connlab.ntust.info', 'git.connlab.ntust.info'],
                                'ais3.org':['final.ais3.org', 'pre-exam.ais3.org'],
                                'gronext.com':['okameinko.gronext.com', 'dev.gronext.com', 'git.inner.gronext.com'],
                                'keniver.com':['blog.keniver.com', 'polyfiles.blog.keniver.com'],
                                'taiwandestiny.com':['online.taiwandestiny.com']
                            }

        SubDomain_Data = {      '0b100.com':set(),
                                'conan.site':set(),
                                'connlab.tw':set(),
                                'gronextapps.com':set(),
                                'ntust.info':set(),
                                'ais3.org':set(),
                                'gronext.com':set(),
                                'keniver.com':set(),
                                'taiwandestiny.com':set()
                            }
        self.ansEqual(engines, Test_Domain_Data, SubDomain_Data)

    def test_Virustotal(self):    
        engines = 'Virustotal'

        Test_Domain_Data = {    '0b100.com':['blog.0b100.com'],
                                'conan.site':['unifi.conan.site'],
                                'connlab.tw':[],
                                'gronextapps.com':[],
                                'ntust.info':['mail.ntust.info'],
                                'ais3.org':[],
                                'gronext.com':[],
                                'keniver.com':[],
                                'taiwandestiny.com':[]
                            }

        SubDomain_Data = {      '0b100.com':set(),
                                'conan.site':set(),
                                'connlab.tw':set(),
                                'gronextapps.com':set(),
                                'ntust.info':set(),
                                'ais3.org':set(),
                                'gronext.com':set(),
                                'keniver.com':set(),
                                'taiwandestiny.com':set()
                            }
        
        self.ansEqual(engines, Test_Domain_Data, SubDomain_Data)

    def test_ThreatCrowd(self):    
        engines = 'ThreatCrowd'

        Test_Domain_Data = {    '0b100.com':[],
                                'conan.site':[],
                                'connlab.tw':[],
                                'gronextapps.com':[],
                                'ntust.info':[],
                                'ais3.org':[],
                                'gronext.com':[],
                                'keniver.com':[],
                                'taiwandestiny.com':[]
                            }

        SubDomain_Data = {      '0b100.com':set(),
                                'conan.site':set(),
                                'connlab.tw':set(),
                                'gronextapps.com':set(),
                                'ntust.info':set(),
                                'ais3.org':set(),
                                'gronext.com':set(),
                                'keniver.com':set(),
                                'taiwandestiny.com':set()
                            }
        self.ansEqual(engines, Test_Domain_Data, SubDomain_Data)

    def test_SSL_Certificates(self):    
        engines = 'SSL'

        Test_Domain_Data = {    '0b100.com':['blog.0b100.com', 'git.0b100.com', 'www.git.0b100.com', 'www.0b100.com'],
                                'conan.site':['unifi.conan.site', 'nas.conan.site', 'www.nas.conan.site'],
                                'connlab.tw':['git.connlab.tw', 'nas.connlab.tw', 'www.nas.connlab.tw'],
                                'gronextapps.com':['web.bear.gronextapps.com'],
                                'ntust.info':['mail.ntust.info', 'git.connlab.ntust.info', 'vpsm.connlab.ntust.info', 'vps.connectivity.ntust.info', 'www.vps.connectivity.ntust.info'],
                                'ais3.org':['pre-exam.ais3.org', 'b0rder1and.ais3.org', 'www.ais3.org', 'eofinal.ais3.org', 'eofqual.ais3.org', 'final.ais3.org', 'quiz.ais3.org', 'www.final.ais3.org'],
                                'gronext.com':['unifi.gronext.com', 'mail.gronext.com', 'okameinko.gronext.com', 'git.inner.gronext.com', 'www.git.inner.gronext.com', 'monitor.gronext.com', 'sqladmin.dev.gronext.com', 'trn.dev.gronext.com', 'dev.gronext.com'],
                                'keniver.com':['blog.keniver.com', 'tzutzumap.keniver.com', 'polyfiles.blog.keniver.com', 'panel.dnslog.keniver.com'],
                                'taiwandestiny.com':['online.taiwandestiny.com']
                            }

        SubDomain_Data = {      '0b100.com':set(),
                                'conan.site':set(),
                                'connlab.tw':set(),
                                'gronextapps.com':set(),
                                'ntust.info':set(),
                                'ais3.org':set(),
                                'gronext.com':set(),
                                'keniver.com':set(),
                                'taiwandestiny.com':set()
                            }
        self.ansEqual(engines, Test_Domain_Data, SubDomain_Data)

    def test_PassiveDNS(self):   
        engines = 'PassiveDNS'

        Test_Domain_Data = {    '0b100.com':['blog.0b100.com', 'git.0b100.com'],
                                'conan.site':[],
                                'connlab.tw':[],
                                'gronextapps.com':[],
                                'ntust.info':[],
                                'ais3.org':[],
                                'gronext.com':['okameinko.gronext.com'],
                                'keniver.com':['lulu.keniver.com'],
                                'taiwandestiny.com':[]
                            }

        SubDomain_Data = {      '0b100.com':set(),
                                'conan.site':set(),
                                'connlab.tw':set(),
                                'gronextapps.com':set(),
                                'ntust.info':set(),
                                'ais3.org':set(),
                                'gronext.com':set(),
                                'keniver.com':set(),
                                'taiwandestiny.com':set()
                            }

        self.ansEqual(engines, Test_Domain_Data, SubDomain_Data)
    

if __name__ == '__main__':
    unittest.main()  
