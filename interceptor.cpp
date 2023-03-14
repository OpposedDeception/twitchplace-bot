#include <iostream>
#include <curl/curl.h>

#define URL "https://place.streamkit.com/PutPixel"

void GET(CURL *curl) {
  curl_easy_setopt(curl, CURLOPT_URL, URL);
  CURLcode res = curl_easy_perform(curl);
  
  if(res != CURLE_OK) {
    std::cerr << "Error sending GET request: " << curl_easy_strerror(res) << std::endl;
  }
}

int main() {
  curl_global_init(CURL_GLOBAL_ALL);
  CURL *curl = curl_easy_init();
  GET(curl);
  curl_easy_cleanup(curl);
  curl_global_cleanup();  
  return 0;
}
