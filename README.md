## Introduction
The present project has the objective of demonstrating the skills and knowledge of the management of Selenium WebDriver.

The project consists of testing the Front-end of a web site. Testing functions, colors, messages, fields and more. We have four test cases, which are divided into two tests. All are executed by the test suite and at the end we can see the final result.

### Test Case 1: Privacy Policy Modal

- Check if the modal is present when loading the page.
- If the security policies are not accepted, the page refreshes and reloads the modal.
- If the security policies are accepted, the modal should no longer be displayed.

### Test Case 2: Query Fields

- Focus on the field, this should change to blue.
- Typing characters and hitting enter the url will change to the characters entered.
- As the folio does not exist, a red banner must be displayed.
- The "pdkwd" folio:
	* Show a banner with title: "Under review"
- With the folio "5dp5e":
	* The banner with the title: "Closed" must be displayed

###Test Case 3: Validate Form

- when clicking on the "Terminar y enviar" button, all the required fields must be shown in red.
- Activate "Dar mis datos personales" the fields" Mobile phone and Full name" should be displayed.
- Activate "Anonymous" the fields "Teléfono móvil y Nombre completo" must be hidden.
- Activate "Propuesta de mejora" the fields "Report/complaint concepts" must be hidden.

###Test Case 4: Complete Form
- When saving the form correctly, a green banner with the text "Folio de seguimiento" should be displayed.
- Click on "Check status" the url should change "/folio number" and a green banner should be displayed with the text: "Abierta".

## Instruction

- Make sure that the "webdriverfactory" file, this contains the Url and Web Driver directions.
- Position ourselves in the main project folder and execute the following command:
		"py.test test/test_suite.py"
