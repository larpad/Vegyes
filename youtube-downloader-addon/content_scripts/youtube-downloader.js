
function addDownloadButton() {
    if (!window.location.pathname.includes('/watch')) return;
    
    const menuContainer = document.querySelector('#top-level-buttons-computed');
    if (!menuContainer || document.querySelector('.marti-download-btn')) return;
    
    const downloadBtn = document.createElement('button');
    downloadBtn.className = 'marti-download-btn';
    downloadBtn.innerHTML = 'Download';
    downloadBtn.style.cssText = `
        background: #cc0000;
        color: white;
        border: none;
        padding: 10px 16px;
        border-radius: 18px;
        cursor: pointer;
        margin-left: 8px;
    `;
    
    downloadBtn.addEventListener('click', () => {
        const videoId = new URLSearchParams(window.location.search).get('v');
        if (videoId) {
            alert('Download started for video: ' + videoId);
        }
    });
    
    menuContainer.appendChild(downloadBtn);
}

// Initial run
addDownloadButton();

// Watch for page changes
new MutationObserver(() => {
    addDownloadButton();
}).observe(document.body, { childList: true, subtree: true });
