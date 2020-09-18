from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import random
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://tinder.com/?lang=en")




driver.implicitly_wait(7)
like_button = WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button'))

    ) 
dislike_button = WebDriverWait(driver, 100).until(
	EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button'))
	)
like_count = 0
dislike_count = 0

action_like = ActionChains(driver)
action_like.click(like_button)

action_dislike = ActionChains(driver)
action_dislike.click(dislike_button)

while(True):
	# random time delay to make it look more like a human
	rand_sleep = random.random()
	time.sleep(rand_sleep)
	rand_liker_disliker = random.random()
	
	#randomly liking and disliking wrt value of random.random() which lie between 0 and 1 
	if rand_liker_disliker < .85:
		action_like.perform()

		print("liked =    ",like_count)
		like_count = like_count + 1
		
		# Giving delay after like_count reaches multiple of 100s
		if like_count % 100 == 0:
			time.sleep(100)
		
		
	else:
		action_dislike.perform()
		print("disliked = ",dislike_count)
		dislike_count = dislike_count + 1



