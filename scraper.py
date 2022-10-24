from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


def get_jobs(link, num_jobs):

    # initiation chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1120, 1000)

    # open url
    url = link
    driver.get(url)
    jobs = []

    # if true still search the jobs, depend how many you want
    while len(jobs) < num_jobs:

        # let page load
        time.sleep(5)

        # click random for trigger pop up
        try:
            driver.find_element(
                By.XPATH, './/*[@id="MainCol"]/div[1]/ul/li[1]').click()
        except NoSuchElementException:
            pass
        time.sleep(3)

        # close popup
        try:
            driver.find_element(
                By.XPATH, './/*[@id="JAModal"]/div/div[2]/span').click()
        except NoSuchElementException:
            pass

        # listing job
        job_buttons = driver.find_elements(
            By.XPATH, './/*[@id="MainCol"]/div[1]/ul/li')  # button for list

        for job_button in job_buttons:

            print("Progress: {}".format(
                "" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_button.click()  # to open description
            time.sleep(1)
            collected_successfully = False

            while not collected_successfully:
                try:
                    company_name = driver.find_element(
                        By.XPATH, './/*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]').text
                    role_job = driver.find_element(
                        By.XPATH, './/*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
                    location = driver.find_element(
                        By.XPATH, './/*[@id="MainCol"]/div[1]/ul/li[2]/div[2]/div[2]/span').text
                    collected_successfully = True
                except:
                    time.sleep(5)

            try:
                salary_estimate = driver.find_element(
                    By.XPATH, './/*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span').text
            except NoSuchElementException:
                salary_estimate = -1  # if not have salary

            try:
                rating = driver.find_element(
                    By.XPATH, './/*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/span').text
            except NoSuchElementException:
                rating = -1

            try:
                size = driver.find_element(
                    By.XPATH, './/*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
            except NoSuchElementException:
                size = -1

            try:
                type_company = driver.find_element(
                    By.XPATH, './/*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span[2]').text
            except NoSuchElementException:
                type_company = -1

            try:
                sector = driver.find_element(
                    By.XPATH, './/*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[2]').text
            except NoSuchElementException:
                sector = -1

            try:
                founded = driver.find_element(
                    By.XPATH, './/*[@id="EmpBasicInfo"]/div[1]/div/div[2]/span[2]').text
            except NoSuchElementException:
                founded = -1

            try:
                industry = driver.find_element(
                    By.XPATH, './/*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[2]').text
            except NoSuchElementException:
                industry = -1

            try:
                revenue = driver.find_element(
                    By.XPATH, './/*[@id="EmpBasicInfo"]/div[1]/div/div[6]/span[2]').text
            except NoSuchElementException:
                revenue = -1

            try:
                driver.find_element(
                    By.XPATH, './/*[@id="JobDescriptionContainer"]/div[2]').click()
                time.sleep(.5)
                desc = driver.find_element(
                    By.XPATH, './/*[@id="JobDescriptionContainer"]').text
            except NoSuchElementException:
                desc = -1

            # input data to jobs
            jobs.append({"Job Title": role_job,
                         "Salary Estimate": salary_estimate,
                         "Rating": rating,
                         "Company Name": company_name,
                         "Description": desc,
                         "Location": location,
                         "size": size,
                         "type": type_company,
                         "sector": sector,
                         "founded": founded,
                         "industry": industry,
                         "revenue": revenue})

        # if one page done find button to the next page
        try:
            driver.find_element(
                By.XPATH, './/*[@id="MainCol"]/div[2]/div/div[1]/button[7]').click()

        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(
                num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)
