from utils.email.entity import TemplateContent, Template

email_template: dict[Template, dict[TemplateContent, str]] = {
    Template.REGISTER_SUCCESS: {
        TemplateContent.HTML: """
<!DOCTYPE html>
<html lang="en-US">
    <head>
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
        <title>New Account Email Template</title>
        <meta name="description" content="New Account Email Template." />
        <style type="text/css">
            a:hover {
                text-decoration: underline !important;
            }
        </style>
    </head>

    <body
        marginheight="0"
        topmargin="0"
        marginwidth="0"
        style="margin: 0px; background-color: #f2f3f8"
        leftmargin="0"
    >
        <table
            cellspacing="0"
            border="0"
            cellpadding="0"
            width="100%"
            bgcolor="#f2f3f8"
            style="
                @import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700);
                font-family: 'Open Sans', sans-serif;
            "
        >
            <tr>
                <td>
                    <table
                        style="
                            background-color: #f2f3f8;
                            max-width: 1000px;
                            margin: 0 auto;
                        "
                        width="100%"
                        border="0"
                        align="center"
                        cellpadding="0"
                        cellspacing="0"
                    >
                        <tr>
                            <td style="height: 80px">&nbsp;</td>
                        </tr>
                        <tr>
                            <td>
                                <table
                                    width="95%"
                                    border="0"
                                    align="center"
                                    cellpadding="0"
                                    cellspacing="0"
                                    style="
                                        max-width: 1000px;
                                        background: #fff;
                                        border-radius: 3px;
                                        text-align: center;
                                        -webkit-box-shadow: 0 6px 18px 0
                                            rgba(0, 0, 0, 0.06);
                                        -moz-box-shadow: 0 6px 18px 0
                                            rgba(0, 0, 0, 0.06);
                                        box-shadow: 0 6px 18px 0
                                            rgba(0, 0, 0, 0.06);
                                    "
                                >
                                    <tr>
                                        <td style="height: 40px">&nbsp;</td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 0 35px">
                                            <h1
                                                style="
                                                    color: #1e1e2d;
                                                    font-weight: 500;
                                                    margin: 0;
                                                    font-size: 32px;
                                                    font-family: 'Rubik',
                                                        sans-serif;
                                                "
                                            >
                                                Welcome {{NAME}} to our website,
                                            </h1>
                                            <p
                                                style="
                                                    font-size: 15px;
                                                    color: #455056;
                                                    margin: 8px 0 0;
                                                    line-height: 24px;
                                                "
                                            >
                                                Your account has been registed
                                                successfully.
                                            </p>
                                            <a
                                                href="{{URL}}"
                                                style="
                                                    background: #20e277;
                                                    text-decoration: none !important;
                                                    display: inline-block;
                                                    font-weight: 500;
                                                    margin-top: 24px;
                                                    color: #fff;
                                                    text-transform: uppercase;
                                                    font-size: 14px;
                                                    padding: 10px 24px;
                                                    display: inline-block;
                                                    border-radius: 50px;
                                                    cursor: pointer;
                                                "
                                                >Login to your Account</a
                                            >
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="height: 40px">&nbsp;</td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="height: 20px">&nbsp;</td>
                        </tr>
                        <tr>
                            <td style="text-align: center">
                                <p
                                    style="
                                        font-size: 14px;
                                        color: rgba(
                                            69,
                                            80,
                                            86,
                                            0.7411764705882353
                                        );
                                        line-height: 18px;
                                        margin: 0 0 0;
                                    "
                                >
                                    &copy; <strong>Nguyen Thanh Tam</strong>
                                </p>
                            </td>
                        </tr>
                        <tr>
                            <td style="height: 80px">&nbsp;</td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
</html>
""",
        TemplateContent.PLAIN_TEXT: """
        Welcome {{NAME}} to our website,
        \nYour account has been registed successfully.
        \nLOGIN TO YOUR ACCOUNT [{{URL}}]
        \n© Nguyen Thanh Tam
    """
    },
    Template.REMINDER_BUYING: {
        TemplateContent.HTML: """
            <!DOCTYPE html>
<html lang="en-US">
    <head>
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
        <title>New Account Email Template</title>
        <meta name="description" content="New Account Email Template." />
        <style type="text/css">
            a:hover {
                text-decoration: underline !important;
            }
        </style>
    </head>

    <body
        marginheight="0"
        topmargin="0"
        marginwidth="0"
        style="margin: 0px; background-color: #f2f3f8"
        leftmargin="0"
    >
        <table
            cellspacing="0"
            border="0"
            cellpadding="0"
            width="100%"
            bgcolor="#f2f3f8"
            style="
                @import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700);
                font-family: 'Open Sans', sans-serif;
            "
        >
            <tr>
                <td>
                    <table
                        style="
                            background-color: #f2f3f8;
                            max-width: 1000px;
                            margin: 0 auto;
                        "
                        width="100%"
                        border="0"
                        align="center"
                        cellpadding="0"
                        cellspacing="0"
                    >
                        <tr>
                            <td style="height: 80px">&nbsp;</td>
                        </tr>
                        <tr>
                            <td>
                                <table
                                    width="95%"
                                    border="0"
                                    align="center"
                                    cellpadding="0"
                                    cellspacing="0"
                                    style="
                                        max-width: 1000px;
                                        background: #fff;
                                        border-radius: 3px;
                                        text-align: center;
                                        -webkit-box-shadow: 0 6px 18px 0
                                            rgba(0, 0, 0, 0.06);
                                        -moz-box-shadow: 0 6px 18px 0
                                            rgba(0, 0, 0, 0.06);
                                        box-shadow: 0 6px 18px 0
                                            rgba(0, 0, 0, 0.06);
                                    "
                                >
                                    <tr>
                                        <td style="height: 40px">&nbsp;</td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 0 35px">
                                            <h1
                                                style="
                                                    color: #1e1e2d;
                                                    font-weight: 500;
                                                    margin: 0;
                                                    font-size: 32px;
                                                    font-family: 'Rubik',
                                                        sans-serif;
                                                "
                                            >
                                                Hi {{NAME}},
                                            </h1>
                                            <p
                                                style="
                                                    font-size: 15px;
                                                    color: #455056;
                                                    margin: 8px 40px 0;
                                                    text-align: left;
                                                    line-height: 24px;
                                                "
                                            >
                                                Greetings from Nguyen Thanh Tam
                                                Company! We hope this message
                                                finds you well. <br />

                                                We noticed that you've
                                                successfully created an account
                                                with us, and we're thrilled to
                                                have you on board. However, it
                                                seems that you haven't made any
                                                transactions yet.
                                            </p>
                                            <a
                                                href="{{URL}}"
                                                style="
                                                    background: #20e277;
                                                    text-decoration: none !important;
                                                    display: inline-block;
                                                    font-weight: 500;
                                                    margin-top: 24px;
                                                    color: #fff;
                                                    text-transform: uppercase;
                                                    font-size: 14px;
                                                    padding: 10px 24px;
                                                    display: inline-block;
                                                    border-radius: 50px;
                                                    cursor: pointer;
                                                "
                                                >Access our website</a
                                            >
                                            <p
                                                style="
                                                    font-size: 15px;
                                                    color: #455056;
                                                    margin: 8px 40px 0;
                                                    line-height: 24px;
                                                    text-align: left;
                                                "
                                            >
                                                To enhance your experience and
                                                unlock exclusive benefits, we
                                                encourage you to make your first
                                                purchase on our platform.
                                                Whether it's exploring our
                                                latest products, enjoying
                                                special promotions, or earning
                                                rewards, there's so much waiting
                                                for you.<br />

                                                Thank you for choosing our
                                                company! We look forward to
                                                serving you, and don't miss out
                                                on the fantastic opportunities
                                                that await.<br /><br />

                                                Best regards,<br />

                                                NTC Company
                                            </p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="height: 40px">&nbsp;</td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="height: 20px">&nbsp;</td>
                        </tr>
                        <tr>
                            <td style="text-align: center">
                                <p
                                    style="
                                        font-size: 14px;
                                        color: rgba(
                                            69,
                                            80,
                                            86,
                                            0.7411764705882353
                                        );
                                        line-height: 18px;
                                        margin: 0 0 0;
                                    "
                                >
                                    &copy; <strong>Nguyen Thanh Tam</strong>
                                </p>
                            </td>
                        </tr>
                        <tr>
                            <td style="height: 80px">&nbsp;</td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
</html>
        """,
        TemplateContent.PLAIN_TEXT: """
    Hi {{NAME}},
    \nGreetings from Nguyen Thanh Tam Company! We hope this message finds you well.
    \nWe noticed that you've successfully created an account with us, and we're thrilled to have you on board. However, it seems that you haven't made any transactions yet.
    \nACCESS OUR WEBSITE [{{URL}}]
    \nTo enhance your experience and unlock exclusive benefits, we encourage you to make your first purchase on our platform. Whether it's exploring our latest products, enjoying special promotions, or earning rewards, there's so much waiting for you.
    \nThank you for choosing our company! We look forward to serving you, and don't miss out on the fantastic opportunities that await.
    \n\nBest regards,
    \nNTC Company
    \n© Nguyen Thanh Tam
"""
    }
}
