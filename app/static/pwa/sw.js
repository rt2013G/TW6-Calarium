let cacheName = 'calarium_cache';
let filesToCache = [
    '../styles/style.css',
    '../main.js',
    '../background.js',
    '../assets/texture/moon.jpg',
    '../assets/texture/normal.jpg',
];

self.addEventListener('install', function(e) {
    e.waitUntil(
        caches.open(cacheName).then(function(cache) {
            return cache.addAll(filesToCache);
        })
    );
});

self.addEventListener('fetch', function(e) {
    e.respondWith(
        caches.match(e.request).then(function(response) {
            return response || fetch(e.request);
        })
    );
});
