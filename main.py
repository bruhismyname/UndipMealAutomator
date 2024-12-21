from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from datetime import datetime
import time
import requests

# inisialisasi driver
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=USERAGENTCHROME") # ganti USERAGENTCHROME dengan user agent anda
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--user-data-dir=USERDATAPROFILE") # ganti USERDATAPROFILE dengan lokasi folder user data anda

driver = uc.Chrome(options=chrome_options)

# URL login
url = "https://sso.undip.ac.id/"

# buka halaman web
driver.get(url)
print("Berhasil membuka halaman web.")

# masukkan username
try:
    # tunggu elemen input ID muncul dan isi data
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="identity"]'))
    ).send_keys('MASUKKAN_USERNAME_SSO_ANDA')
    print("Berhasil masukkan Username.")
except TimeoutException:
    print("Error.")

# klik tombol login
try:
    # klik login
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/section/div/div/div/div[2]/div/form/button'))
    ).click()
    print("Sudah klik login.")
except TimeoutException:
    print("Error.")

try:
    # masukkan password
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="i0118"]'))
    ).send_keys('MASUKKAN_PASSWORD_SSO_ANDA')
    print("Berhasil masukkan password.")
except TimeoutException:
    print("Error.")

try: 
    # klik tombol sign in
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="idSIButton9"]'))
    ).click()
    print("Berhasil klik tombol sign in.")
except TimeoutException:
    print("Error.")

try:
    # klik tombol form
    element = driver.find_element(By.XPATH, '//*[@id="minimal-statistics-bg"]/div[3]/div[2]/div[2]/div/div[4]/a/div/div/div')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    print("Berhasil klik menu form.")
except TimeoutException:
    print("Error.")

# tunggu sampai halaman form muncul
WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)

# beralih ke halaman form
new_tab = driver.window_handles[-1]
driver.switch_to.window(new_tab)

# melanjutkan tab baru
print("Sudah beralih ke tab kedua:", driver.title)

# klik tombol Pendaftaran Makanan Sehat
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Pendaftaran Makanan Sehat"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    print("Berhasil klik menu Pendaftaran Makanan Sehat.")
except TimeoutException:
    print("Error.")

# tunggu sampai halaman form muncul
WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)

# Beralih ke halaman form
new_tab2 = driver.window_handles[-1]
driver.switch_to.window(new_tab2)

# Melanjutkan tab baru
print("Sudah beralih ke tab ketiga:", driver.title)

# waktu target untuk menjalankan kode (format: HH:MM:SS, 24 jam)
target_time = "10:00:00"

def wait_until_target_time(target_time):
    print(f"Menunggu hingga waktu {target_time}...")
    while True:
        # ambil waktu sekarang
        now = datetime.now().strftime("%H:%M:%S")
        if now == target_time:
            print("Waktu yang diinginkan telah tiba.")
            break
        time.sleep(1)  # cek setiap 1 detik (atau sesuai kebutuhan)
# tunggu hingga waktu target untuk merefresh
wait_until_target_time(target_time)

# refresh halaman web pada waktu yang diinginkan
print("Merefresh halaman web...")
driver.refresh()
print("Berhasil merefresh web")

try:
    # tanggal dan tempat
    element=WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-tanggal-container"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    print("Berhasil klik pilih tanggal")
    # pilih elemen berdasarkan tanggal dan lokasi
    tanggal = "Kamis, 19 Desember 2024" # contoh tanggal
    lokasi = "Auditorium FPIK"          # contoh lokasi

    # XPath dinamis untuk mencocokkan tanggal dan lokasi
    xpath_dynamic = f"//li[contains(text(), '{tanggal}') and contains(text(), '{lokasi}')]"

    # tunggu hingga elemen tersedia dan klik
    option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_dynamic)))
    option.click()

    print("Berhasil memilih tanggal dan lokasi!")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")

# API Key dan data reCAPTCHA
api_key = "API_KEY_2CAPTCHA"
site_key = "SITE_KEY_CAPTCHA_2CAPTCHA"
page_url = "https://form.undip.ac.id/makanansehat/pendaftaran"

# kirim CAPTCHA untuk diselesaikan oleh 2Captcha
payload = {
    "key": api_key,
    "method": "userrecaptcha",
    "googlekey": site_key,
    "pageurl": page_url
}

session = requests.Session()
response = session.post("https://2captcha.com/in.php", data=payload, timeout=10)

if response.text.startswith("OK|"):
    captcha_id = response.text.split("|")[1]
    print(f"CAPTCHA ID diterima: {captcha_id}")
    
    # periksa status penyelesaian CAPTCHA
    status_url = f"https://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}"
    while True:
        status_response = session.get(status_url, timeout=10)
        if status_response.text.startswith("OK|"):
            solution = status_response.text.split("|")[1]
            print(f"CAPTCHA berhasil diselesaikan: {solution}")
            break
        else:
            print("Menunggu penyelesaian CAPTCHA...")
            time.sleep(2)  # tunggu 2 detik sebelum mencoba lagi
else:
    print(f"Error mengirim CAPTCHA: {response.text}")
    exit()

# selenium: gunakan hasil penyelesaian CAPTCHA pada halaman
try:
    # tunggu elemen reCAPTCHA tersedia di halaman
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "g-recaptcha-response"))
    )
    print("Elemen reCAPTCHA ditemukan.")

    # terapkan solusi CAPTCHA dengan execute_script
    driver.execute_script(
        f"document.getElementById('g-recaptcha-response').innerHTML = '{solution}'"
    )
    print("Solusi CAPTCHA diterapkan.")
except:
    print("Terjadi kesalahan saat menyimpan solusi CAPTCHA.")

input("Masukkan CAPTCHA dan tekan Enter...") # Untuk captcha manual (tidak menggunakan 2Captcha)

# klik simpan
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="reg_ddart_covid"]/div/div[9]/button'))
).click()

# klik accept saat alert muncul
WebDriverWait(driver, 5).until(EC.alert_is_present())
alert = Alert(driver)
alert.accept()

# tambahkan sleep jika perlu (opsional)
time.sleep(120)
