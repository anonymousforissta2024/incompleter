#Source: https://stackoverflow.com/questions/57213890/python-nmap-typeerror-list-indices-must-be-integers-or-slices-not-str
print(nm_scanner)

{
  'nmap': {
    'command_line': 'nmap -oX - -p 80 -O 192.168.0.1',
    'scaninfo': {
      'tcp': {
        'method': 'syn',
        'services': '80'
      }
    },
    'scanstats': {
      'timestr': 'Fri Jul 26 11:31:30 2019',
      'elapsed': '6.36',
      'uphosts': '1',
      'downhosts': '0',
      'totalhosts': '1'
    }
  },
  'scan': {
    '192.168.0.1': {
      'hostnames': [
        {
          'name': '',
          'type': ''
        }
      ],
      'addresses': {
        'ipv4': '192.168.0.1',
        'mac': '1C:5F:2B:53:45:4F'
      },
      'vendor': {
        '1C:5F:2B:53:45:4F': 'D-Link International'
      },
      'status': {
        'state': 'up',
        'reason': 'arp-response'
      },
      'uptime': {
        'seconds': '87161',
        'lastboot': 'Thu Jul 25 11:18:49 2019'
      },
      'tcp': {
        80: {
          'state': 'open',
          'reason': 'syn-ack',
          'name': 'http',
          'product': '',
          'version': '',
          'extrainfo': '',
          'conf': '3',
          'cpe': ''
        }
      },
      'portused': [
        {
          'state': 'open',
          'proto': 'tcp',
          'portid': '80'
        },
        {
          'state': 'closed',
          'proto': 'udp',
          'portid': '42514'
        }
      ],
      'osmatch': [
        {
          'name': 'Allied Telesyn AT-GS950 or D-Link DES-3226L switch or D-Link DSL-2750U router',
          'accuracy': '100',
          'line': '2603',
          'osclass': [
            {
              'type': 'switch',
              'vendor': 'Allied Telesyn',
              'osfamily': 'embedded',
              'osgen': None,
              'accuracy': '100',
              'cpe': [
                'cpe:/h:alliedtelesyn:at-gs950'
              ]
            },
            {
              'type': 'switch',
              'vendor': 'D-Link',
              'osfamily': 'embedded',
              'osgen': None,
              'accuracy': '100',
              'cpe': [
                'cpe:/h:dlink:des-3226l',
                'cpe:/h:dlink:dsl-2750u'
              ]
            }
          ]
        }
      ]
    }
  }
}