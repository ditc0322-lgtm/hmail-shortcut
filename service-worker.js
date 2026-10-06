// 최소 서비스 워커
// 이 앱은 하나메일로 바로 이동하는 바로가기이므로 별도 캐싱 로직 없이
// PWA 설치 조건(서비스 워커 등록)만 만족시키는 용도로 사용합니다.

self.addEventListener("install", (event) => {
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  self.clients.claim();
});

// 네트워크 요청은 그대로 통과시킴 (캐싱하지 않음)
self.addEventListener("fetch", (event) => {
  event.respondWith(fetch(event.request));
});
