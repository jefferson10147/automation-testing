# Automation test for Amazon

## ![Python_logo_Selenium](https://i.ibb.co/p22K38X/selenium-with-python.png)

## Automation App

<table>
    <tr>
        <td>
            Test Automation practices in Amazon's main website. Using Selenium and Behave libraries with Python. Taking into consideration the Base Page object model. For the automation testing execution, using the Chrome browser and Chrome dev tools.
        </td>
    </tr>
</table>

### Testing page

The page that is being used for all scenarios test cases is [Amazon official website](https://www.amazon.com)

![amazon_logo](https://guiaimpresion.com/wp-content/uploads/2020/06/Logotipo-Amazon-300x169.jpg)

## Installation and Usage (UNIX Systems)

1- Clone this project, on your local machine:

```bash
$git clone https://github.com/jefferson10147/automation-testing.git
```

2- Create a Python virtual environment:

```bash
$python3 -m venv ./your_venv
```

3- Activate env:

```bash
$source your_venv/bin/activate
```

4- Install dependencies:

```bash
$pip install -r requirements.txt
```

5- Download and setup the chromedriver inside your project root directory.

6- Create and set up the .env file, this file will contain all urls, endpoints, and the path for the chromedriver:

```env
CHROME_DRIVER_PATH=your_chromedriver_path
BASE_PAGE=https://www.amazon.com/
SIGNIN_PAGE=amazon_sign_page_url
HELP_PAGE=amazon_help_page_url
BEST_SELLERS=amazon_bestsellers_page_url
HELP_CUSTOMER=amazon_help_customer_page_url
PRODUCT_PAGE=amazon_product_page_url
WHOLEFOODS=amazon_wholefoods_page_url
T_AND_C_PAGE=amazon_t&c_page_url
```

7- Execute any gherkin feature file with multiple scenarios:

```bash
$behave features/tests/your_gerking_file.feature
```

You may execute a specific scenario in Gherkin feature file, using the flag -n:

```bash
$behave features/tests/your_gerking_file.feature -n "Scenario test case description"
```

Examples:

* To run all test cases inside any Gherkin feature file:

```bash
$behave features/tests/amazon_cart.feature
```

* To run any a specific scenario in Gherkin feature file:

```bash
$behave features/tests/amazon_cart.feature -n "User verify cart is empty"
```
