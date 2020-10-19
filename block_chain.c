9#include "./esppl_functions.h"
#define LIST_SIZE 2
#define RELAY_PIN D0
unsigned long key_detected_time;

//这里填手机的MAC地址
uint8_t keymac[LIST_SIZE][ESPPL_MAC_LEN] = {
   {0x11, 0x11, 0x11, 0x11, 0x11, 0x11}
  ,{0x22, 0x22, 0x33, 0x44, 0x55, 0x66}
  };

String devicename[LIST_SIZE] = {
   "device 1"
  ,"device 2"
  };

bool maccmp(uint8_t *mac1, uint8_t *mac2) {
  for (int i=0; i < ESPPL_MAC_LEN; i++) {
    if (mac1[i] != mac2[i]) {
      return false;
    }
  }
  return true;
}

void cb(esppl_frame_info *info) {
  for (int i=0; i<LIST_SIZE; i++) {
    if (maccmp(info->sourceaddr, keymac[i]) || maccmp(info->receiveraddr, keymac[i])) {
      Serial.printf("\n%s is here!", devicename[i].c_str());
      key_detected_time = millis();
    }
  }
}

void setup() {
  delay(500);
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);
  esppl_init(cb);
  key_detected_time = millis() - 6000000;
}

void loop() {
  esppl_sniffing_start();
  while (true) {
    for (int i = ESPPL_CHANNEL_MIN; i <= ESPPL_CHANNEL_MAX; i++ ) {
      esppl_set_channel(i);
      while (esppl_process_frames()) {
        //
      }
      // 如果10分钟之内有检测到指定设备
      if (millis() - key_detected_time < 600000) {
        digitalWrite(RELAY_PIN, HIGH);
      } else {
        digitalWrite(RELAY_PIN, LOW);
      }
    }
  }  
}