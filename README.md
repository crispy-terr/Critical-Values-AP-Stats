[README.txt](https://github.com/crispy-terr/Test-Stat-Calculator/files/14551389/README.txt)
Program Name: Critical Values for Significance Tests

Written by: Cristian Cannella

Date: March 10th, 2024

Description:

This Python script serves as a tool for calculating critical values for significance tests, namely t* and z* values. The script provides functions for both one-sample and two-sample t-tests, as well as one-sample and two-sample z-tests. Users are prompted to input relevant parameters such as sample means, standard deviations, sample sizes, and population means, where applicable.

How to Use:

Running the Script:

Execute the script in a Python environment.
Follow the prompts to select the desired type of test (t* or z*) and the specific test scenario (one-sample or two-sample).
Input Parameters:

For one-sample tests, input parameters include sample mean (x-bar), population mean (mu), standard deviation (std. dev), and sample size (n).
For two-sample tests, input parameters vary based on the scenario. For population 1 and 2, input sample means (x-bar), standard deviations (std. dev), and sample sizes (n). Additionally, input the difference between population means (mu1-mu2) when prompted.
For z-tests, input parameters include sample proportions (p-hat), null hypothesis proportions (p-naught), and sample size (n). In the case of two-sample z-tests, input sample proportions and sample sizes for both populations, along with the difference between null hypothesis proportions (p-naught1-p-naught2).
Output:

The script calculates and outputs the corresponding critical value (t* or z*) based on the provided input parameters.
Exiting the Script:

To exit the script, choose the "Exit" option when prompted for the type of test.
Disclaimer:

This script assumes familiarity with statistical significance testing and the interpretation of critical values. It is essential to ensure the correctness of input parameters and understand the underlying assumptions of each statistical test before interpreting the results.
