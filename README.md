# Python_Selenium_QA

### Excersie expectations

The goal of this project is to test the following log-in webpage https://app.sysdigcloud.com/#/login

### Prerequisites

First, we need to install the Selenium framework: \
`pip3 install selenium` \
We can confirm the installation like this:

```bash
pip3 list | grep selenium
selenium                      4.2.0
```

Then we will need a web driver, in this case, I will be using Chrome to make the test. The link is on the following [page](https://sites.google.com/chromium.org/driver/) \
Make sure that you add the executable driver to the `$PATH` env variable once installed.

### Usage

Install the repository: \
`git clone https://github.com/S3B4SZ17/Python_Selenium_QA.git` \

There are 2 options to run the Script:

```bash
cd Python_Selenium_QA
python3 login.py -u username@domain.com
```

or

```bash
cd Python_Selenium_QA
chmod u+x login.py
./login.py -u username@domain.com -p password_test
```

You can run it with the `-h` option to see the information of all the parameter flags. If no flags are specified the default options will be used.

### Improvements

- If we could have more time we can validate the format of the username and password to see if they meet minimum security constraints and best practices.
- We could also test the response times of the page.
- Check the other login options, if using Google, SAML or OpenID
- We can also check the response times, and functionality and see if there are any changes or errors when using a different region.
