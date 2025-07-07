{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "95fa229d-8064-4bda-b956-6283289328f3",
   "metadata": {},
   "source": [
    "<h1/><b/>Basic Data Cleaning Code</b></h1>\n",
    "<h2/><b/>Background</b></h2>\n",
    "\n",
    "This mini project is focused on the basic steps in data cleaning. I have tried to comment the code out so that I (and others) can understand what the code is and what it's doing.  \n",
    "\n",
    "To help debug the code, I asked ChatGPT to help debug it.  The goal is to do these mini projects in a short amount of time (my goal is an hour).  When I realized it was taking too long and towards the end, I used  the AI Assistant in Anaconda since ChatGPT continued to provide code and even debugging code that was incorrect. The Anaconda AI Assistant sped up the debugging process significantly.  \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "03a3c599-6bf5-4f6a-adf4-8b0a025583ee",
   "metadata": {},
   "source": [
    "<div style=\"border: 2px solid black; padding: 10px;\">\n",
    "<span style=\"color: blue;\"><h3/><b/>Identify the data cleaning steps</b></h3></span>\n",
    "\n",
    "1. Load data\n",
    "2. Remove duplicates\n",
    "3. Fill or flag missing values\n",
    "4. Standardize date formats\n",
    "5. Clean up the columns for the end user\n",
    "6. Output a clean version of the file\n",
    "\n",
    "</div>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0e27063c-fd1f-4a32-a5de-65c4e9cb31f6",
   "metadata": {},
   "source": [
    "<h2><b>Develop and execute data cleaning code</b></h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "078cc80f-ee3b-4fce-9669-8d3e0e83506c",
   "metadata": {},
   "source": [
    "<div style=\"border: 2px solid black; padding: 10px;\">\n",
    "<span style=\"color: blue;\"><h3/><b/>Step 1: Load libraries and data</b></h3></span>\n",
    "    Make sure that your file is in a location where the application (whether it's text editor or Jupyter Notebook) can read it.\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e310289-248c-4a37-8eeb-58feb43ddc5b",
   "metadata": {},
   "source": [
    "<div style=\"border: 2px solid black; padding: 10px;\">\n",
    "<span style=\"color: blue;\"><h3/><b/>Step 1: Load libraries and data</b></h3></span>  \n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "36904665-b486-427a-9090-1806eb4c998b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   id   name    date_column\n",
      "0   1  Alice     2025/01/01\n",
      "1   2    Bob     01-02-2025\n",
      "2   2    Bob            NaN\n",
      "3   4  David  March 4, 2025\n",
      "4   5    NaN     2025.05.05\n"
     ]
    }
   ],
   "source": [
    "#load libraries\n",
    "import pandas as pd\n",
    "\n",
    "# Step 1: Load your data\n",
    "raw_data = pd.read_csv('/Users/public/data_cleaning.csv')\n",
    "\n",
    "#see what your data looks like. I do this so that I can see if it executed the way I intended. \n",
    "print(raw_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6aae2937-fe06-489c-a75a-94af72b12cc8",
   "metadata": {},
   "source": [
    "<div style=\"border: 2px solid black; padding: 10px;\">\n",
    "<span style=\"color: blue;\"><h3/><b/>Step 2: Remove duplicates</b></h3></span>  \n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f755836e-70fd-4001-a6af-6bbb423bcf50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   id   name    date_column\n",
      "0   1  Alice     2025/01/01\n",
      "1   2    Bob     01-02-2025\n",
      "2   2    Bob            NaN\n",
      "3   4  David  March 4, 2025\n",
      "4   5    NaN     2025.05.05\n"
     ]
    }
   ],
   "source": [
    "#step 2: Remove duplicates\n",
    "raw_data = raw_data.drop_duplicates()\n",
    "print(raw_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d5c0c9f3-f140-4510-ae78-5f7a99face37",
   "metadata": {},
   "source": [
    "<div style=\"border: 2px solid black; padding: 10px;\">\n",
    "<span style=\"color: blue;\"><h3/><b/>Steps 3-5: Clean up data</b></h3></span>  \n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b63c7b2e-0faa-4792-801a-9c99b448c8a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "from dateutil.parser import parse \n",
    "\n",
    "def parse_mixed_dates(date_str):\n",
    "    try:\n",
    "        return datetime.datetime.strptime(date_str, '%m-%d-%Y')\n",
    "    except (ValueError, TypeError):\n",
    "        try:\n",
    "            return parse(date_str)\n",
    "        except:\n",
    "            return None\n",
    "\n",
    "raw_data['standard_dt'] = raw_data['date_column'].apply(parse_mixed_dates)\n",
    "\n",
    "raw_data['formatted_dt'] = raw_data['standard_dt'].dt.strftime('%m-%d-%Y')\n",
    "\n",
    "raw_data['formatted_dt'] = raw_data['formatted_dt'].fillna('--')\n",
    "\n",
    "raw_data = raw_data.rename(columns={'formatted_dt': 'Date'})\n",
    "\n",
    "raw_data.drop(columns=['date_column', 'standard_dt'], inplace=True)\n",
    "\n",
    "cleaned_data = raw_data\n",
    "\n",
    "print(cleaned_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e7ee41bc-03ff-4d23-98ff-bb47c0442760",
   "metadata": {},
   "source": [
    "<div style=\"border: 2px solid black; padding: 10px;\">\n",
    "<span style=\"color: blue;\"><h3/><b/>Step 3-5: Clean up the data by changing it to the correct data type, correct format, and fill in missing values</b></h3></span>\n",
    "    This helps ensure that people know that the data is complete and reliable.\n",
    "\n",
    "The code used: \n",
    "<code>\n",
    "import datetime\n",
    "from dateutil.parser import parse <code>\n",
    "\n",
    "<code>def parse_mixed_dates(date_str):<code>\n",
    "<code>    try:<code>\n",
    "    <code>return datetime.datetime.strptime(date_str, '%%m-%d-%Y')<code>\n",
    "        <code>except (ValueError, TypeError):<code>\n",
    "        <code>try:<code>\n",
    "      <code>      return parse(date_str)<code>\n",
    "        <code>except:<code>\n",
    "            <code>return None<code>\n",
    "\n",
    "<code>raw_data['standard_dt'] = raw_data['date_column'].apply(parse_mixed_dates)<code>\n",
    "\n",
    "<code>raw_data['formatted_dt'] = raw_data['standard_dt'].dt.strftime('%m-%d-%Y')<code>\n",
    "\n",
    "<code>raw_data['formatted_dt'] = raw_data['formatted_dt'].fillna('--')<code>\n",
    "\n",
    "<code>print(raw_data)<code></br>\n",
    "\n",
    "<hr style=\"border: none; height: 2px; background-color: gray;\" />\n",
    "\n",
    "<h3> Test the dates</h3></br>\n",
    "\n",
    "<b><h4>Step A. Import the module and library to make the needed changes.</h4></b>\n",
    "\n",
    "<b>Import the library, function, and module to do the work</b>\n",
    "\n",
    "<code>import datetime \n",
    "from dateutil.parser import parse</code>\n",
    "\n",
    "<b>a. Define the parse_mixed_dates function which takes dates that are in different date formats and puts them into one format (string type).</br>\n",
    "\n",
    "</b>b. Convert the dates to a specific format\n",
    "<code>def parse_mixed_dates(date_str): \n",
    "    try:\n",
    "        return datetime.datetime.strptime(date_str, '%m-%d-%Y') </code>\n",
    "\n",
    "<b>c. The except command is what happens if the above code doesn't work becuase of the type error (if it's not a string) or a format error (not in the specified format). \n",
    "<code>    except (ValueError, TypeError): </code>\n",
    "\n",
    "<b>d. The try command is telling the program to then try to automatically figure out the format (that's what the parse() command does from the dateutil library.\n",
    "        <cocde>try:\n",
    "                return parse(date_str)</code>\n",
    "<b>e. The except command is basically saying that if the specified format command doesn't work and the parse() command doesn't work, then return 'None' so that the program doesn't fail and the data looks complete.\n",
    "            <code>except:\n",
    "            return None </code>\n",
    "\n",
    "\n",
    "<h3> Standardize the dates, convert to the desired format</h3></br>          \n",
    "\n",
    "<code>raw_data['standard_dt'] = raw_data['date_column'].apply(parse_mixed_dates)</code>\n",
    "\n",
    "<code>raw_data['formatted_dt'] = raw_data['standard_dt'].dt.strftime('%m-%d-%Y')</code>\n",
    "\n",
    "<h3> Fill in any NaN (not a number) with '--' and rename column to 'Date'</h3> </br>\n",
    "This helps people know that the data is complete, especially for those using assistive technology. \n",
    "\n",
    "<code>raw_data['formatted_dt'] = raw_data['formatted_dt'].fillna('--')</code>\n",
    "<code>raw_data = raw_data.rename(columns={'formatted_dt': 'Date'})\n",
    "<code>cleaned_data = raw_data\n",
    "\n",
    "\n",
    "<h4> \"Print\" the data so that you can see if the code worked</h4>\n",
    "<code>print(cleaned_data)</code>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9c1da1e-4462-4c69-91a3-840bb288126e",
   "metadata": {},
   "outputs": [],
   "source": [
    "<div style=\"border: 2px solid black; padding: 10px;\">\n",
    "<span style=\"color: blue;\"><h3/><b/>Steps 6: Export or save file & validate location</b></h3></span>  \n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "id": "3fa593de-12f6-4047-b7af-1841af67f626",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File saved to: /Users/public/mp_cleaned_data.csv\n"
     ]
    }
   ],
   "source": [
    "cleaned_data.to_csv('/Users/public/mp_cleaned_data.csv', index=False)\n",
    "\n",
    "file_path = '/Users/public/mp_cleaned_data.csv'\n",
    "cleaned_data.to_csv(file_path, index=False)\n",
    "print(f\"File saved to: {file_path}\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5178008d-bdf0-43b6-8d4e-9d924d3c6030",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
