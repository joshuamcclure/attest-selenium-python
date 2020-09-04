*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.
Library           SeleniumLibrary
Library           ../attest_selenium_python/robotlib.py    HRA11y  Login  html,xml,csv  ./testing-results/a11y

*** Variables ***
${SERVER}         hra11y.com
${BROWSER}        headlessfirefox
${DELAY}          0
${VALID USER}     jmcclure
${VALID PASSWORD}    123@123
${LOGIN URL}      http://${SERVER}/login
${WELCOME URL}    http://${SERVER}/

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Login Page Should Be Open

Login Page Should Be Open
    Does not contain accessibility violations
    # Run accessibility tests
    Title Should Be    - HR A11y

Go To Login Page
    Go To    ${LOGIN URL}
    Login Page Should Be Open

Input Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit Credentials
    Click Button    //*[@id="__next"]/div/form/button

Welcome Page Should Be Open
    Location Should Be    ${WELCOME URL}