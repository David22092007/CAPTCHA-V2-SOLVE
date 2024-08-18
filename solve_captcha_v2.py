def solve_captcha():
        global driver
        for i in range (2):
            try:
                    WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
                    break
            except:
                    None
            if i==1:
                print ('--LỖI-THAO-TÁC--')    
                exit()        
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframes[0])
        for i in range (2):
            try:
                    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "recaptcha-checkbox-border")))
                    break
            except:
                    None
            if i==1:
                print ('--LỖI-THAO-TÁC--')    
                exit()                
        driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()
        sleep(3)
        driver.switch_to.default_content()
        frames = driver.find_elements(By.TAG_NAME,"iframe")
        driver.switch_to.frame(frames[-1])
        try:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "recaptcha-audio-button")))
                driver.find_element(By.ID,"recaptcha-audio-button").click()
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "audio-source")))
                src=driver.find_element(By.ID,"audio-source").get_attribute("src")
                with open('audio\\audio.mp3','wb') as f:
                        f.write(requests.get(src).content)
                sound = AudioSegment.from_mp3("audio\\audio.mp3")
                sound.export("audio\\audio.wav", format="wav")

                # Khởi tạo Recognizer
                recognizer = sr.Recognizer()

                # Mở file WAV
                with sr.AudioFile("audio\\audio.wav") as source:
                    audio_data = recognizer.record(source)

                # Nhận diện giọng nói trong file âm thanh
                try:
                    text = recognizer.recognize_google(audio_data, language="en-US")
                    print("Nội dung nhận diện được: ", text)
                except sr.UnknownValueError:
                    print("Không thể nhận diện được âm thanh.")
                except sr.RequestError as e:
                    print(f"Lỗi khi kết nối với dịch vụ nhận diện: {e}")
                driver.find_element(By.ID,"audio-response").send_keys(text.lower())
                driver.find_element(By.ID,"audio-response").send_keys(Keys.ENTER)
                sleep(3)
                driver.switch_to.default_content()
                frames = driver.find_elements(By.TAG_NAME,"iframe")
                driver.switch_to.frame(frames[0])
                rsp= (driver.find_elements(By.TAG_NAME, "span"))
                for i in rsp:
                        if i.get_attribute('role')=="checkbox":
                            print (i.get_attribute('class'))
                            if i.get_attribute('class')=="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-checked" or i.get_attribute('class')=="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-focused recaptcha-checkbox-checked" or i.get_attribute('class')=="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-checked recaptcha-checkbox-focused":                                                                      
                                    print ('Đã Xác Minh Thành Công ✅')
                                    return True
                            else:
                                    print ('GIẢI KHÔNG THÀNH CÔNG ❎')
                                    return False
        except:
                print ('--LỖI KHÔNG GIẢI ĐƯỢC CAPTCHA AUDIO-- TIẾN HÀNH KIỂM TRA --')
                sleep(3)
                driver.switch_to.default_content()
                frames = driver.find_elements(By.TAG_NAME,"iframe")
                driver.switch_to.frame(frames[0])
                rsp= (driver.find_elements(By.TAG_NAME, "span"))
                for i in rsp:
                        if i.get_attribute('role')=="checkbox":
                            print (i.get_attribute('class'))
                            if i.get_attribute('class')=="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-checked" or i.get_attribute('class')=="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-focused recaptcha-checkbox-checked" or i.get_attribute('class')=="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-checked recaptcha-checkbox-focused":                                                                      
                                    print ('Đã Xác Minh Thành Công ✅')
                                    return True
                            else:
                                    print ('GIẢI KHÔNG THÀNH CÔNG ❎')
                                    return False
