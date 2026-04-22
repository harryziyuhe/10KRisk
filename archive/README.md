# Extracting Texts from 10-K Filings

## Preparation

1. **Create `identity.json` File**  
   In the root directory of the project, create a file called `identity.json` and store your email address in the following format:

   ```json
   {
       "name": "youremail@address.com"
   }
   ```

2. **Customize Ticker List**  
   Edit the `ticker_list.txt` file, located in the root directory, to include the list of tickers you want to analyze. Each ticker should be on a new line.

## Execution

To run the analysis, execute the following command in your terminal:

```bash
python edgar.py
```

This will begin extracting texts from the 10-K filings for the tickers listed in `ticker_list.txt`.

## Additional Information

- Ensure you have the required dependencies installed for the project:
  
- `pandas` for data manipulation
- `requests` for making HTTP requests
- `sec_downloader` for SEC filing downloads
- `sec_parser` for parsing the downloaded filings
- `tqdm` for progress bars

  You can install them using:

  ```bash
  pip install -r requirements.txt
  ```

- **Compliance with SEC Guidelines**  
  If your project relies on the SEC EDGAR API, please ensure you follow the [SEC's fair usage guidelines](https://www.sec.gov/os/accessing-edgar-data) to avoid overloading their systems or violating their terms of service.

- **Email Identity**  
  The `identity.json` file containing your email is used to identify yourself when making requests to the SEC API, which is required for accessing EDGAR data.

- **Customizing Analysis**  
  You can modify the tickers you want to analyze by editing the `ticker_list.txt` file. Each ticker should be placed on a new line. Only those tickers will be included in the analysis.

- **Logging & Errors**  
  Make sure to review any error logs that may be generated during execution, especially if you're not receiving the expected data from the SEC API.

## Contact

For issues or further assistance, feel free to reach out via email: zih028@ucsd.com.
