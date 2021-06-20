import email
import email.mime.base
import email.mime.multipart
import email.mime.text
import logging
import smtplib

logger = logging.getLogger(
    __name__,
)


def execute(
        parameters,
        transfer,
    ):
    smtp_header_from = parameters['smtp_header_from']
    smtp_header_to = parameters['smtp_header_to']
    smtp_host = parameters['smtp_host']
    smtp_password = parameters['smtp_password']
    smtp_port = parameters['smtp_port']
    smtp_username = parameters['smtp_username']

    reference = transfer['reference']
    subject = f'Currency exchange through Wise for {reference}'
    # FIXME
    msg = 'X € must be transferred to Wise\'s escrow account to add $4.3 to the USD Wise balance.'
    #      ^^^                                                      ^^^^        ^^^

    smtp = smtplib.SMTP_SSL(
        smtp_host,
        port=smtp_port,
    )

    smtp.login(
        smtp_username,
        smtp_password,
    )

    msg_root = email.mime.multipart.MIMEMultipart(
    )
    msg_root['Subject'] = subject
    msg_root['From'] = smtp_header_from
    msg_root['To'] = smtp_header_to

    msg_alternative = email.mime.multipart.MIMEMultipart(
        'alternative',
    )
    msg_root.attach(
        msg_alternative,
    )
    msg_text = email.mime.text.MIMEText(
        msg,
    )
    msg_alternative.attach(
        msg_text,
    )
    smtp.sendmail(
        smtp_header_from,
        smtp_header_to,
        msg_root.as_string(
        ),
    )
