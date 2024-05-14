#Source: https://stackoverflow.com/questions/54803231/how-to-fix-attributeerror-environments-in-odoo
import skpy
import logging
import threading
import odoo

DB_NAME = 'odootest'
UID = odoo.SUPERUSER_ID

_logger = logging.getLogger(__name__)


registry = odoo.modules.registry.Registry.new(DB_NAME)
CR = registry.cursor()
ENV = odoo.api.Environment(CR, UID, {})


class MySkype(skpy.SkypeEventLoop):

    def onEvent(self, event):
        if isinstance(event, skpy.SkypeNewMessageEvent):
            _logger.info('--------' * 5)
            _logger.warning(event)
            _logger.info('--------' * 5)

            message = ('New message from user {} at {}: \'{} \''.format(event.msg.userId,
                                                                     event.msg.time.strftime('%H:%M dd. %d.%m.%Y'),
                                                                     event.msg.content))

            _logger.info('--------' * 5)
            _logger.warning(message)
            _logger.info('--------' * 5)

            partner_id = ENV['res.users'].search([('id', '=', 2)]).partner_id.id

            _logger.info('--------' * 5)
            _logger.warning(partner_id)
            _logger.info('--------' * 5)

            ENV['mail.message'].create({'message_type': 'notification',
                                             'subtype': ENV.ref('mail.mt_comment').id,
                                             'body': message,
                                             'subject': 'Message subject',
                                             'partner_ids': [(4, partner_id), ],
                                             })
            _logger.info('--------' * 5)
            _logger.warning('send')
            _logger.info('--------' * 5)


sk = MySkype('+3767', '12qW', autoAck=True)
thread = threading.Thread(target=sk.loop)
thread.start()