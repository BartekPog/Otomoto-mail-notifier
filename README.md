# OTOMOTO Search notifier

Get an email when a car matching your requirements is posted on [Otomoto](https://otomoto.pl/).

##### Requirements

- Python 3
- Selenium web driver
- New Gmail account with [enabled insecure apps](https://hotter.io/docs/email-accounts/secure-app-gmail/)
- Google Chrome

##### Env variables

| Key            | Description                                          | Example                                                                                                                                                                                                                   |
| -------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MAIL_RECEIVER  | Email address of the person that should get notified | you@mail.com                                                                                                                                                                                                              |
| GMAIL_EMAIL    | Bot's account Gmail address                          | yourBot@gmail.com                                                                                                                                                                                                         |
| GMAIL_PASSWORD | Password to the bot account                          | admin                                                                                                                                                                                                                     |
| OFFERS_URL     | Url to the search page with applied filters          | **[This url](https://www.otomoto.pl/osobowe/zuk/katowice/?search%5Bfilter_float_price%3Ato%5D=40000&search%5Border%5D=created_at%3Adesc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bdist%5D=115&search%5Bcountry%5D=)** |

##### Instalation steps

1. Start by cloning this repository.

1. Create a way of securely storing environment variables, or paste them into the `sourceConfExample.sh`

1. Then add the script to your CRONtab
   For example:
   `0 */2 * * * source pathToRepo/sourceConfExample.sh && python3 pathToRepo/main.py`
