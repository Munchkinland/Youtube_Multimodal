document.addEventListener('DOMContentLoaded', () => {
    const transcribeBtn = document.getElementById('transcribe-btn');
    const askBtn = document.getElementById('ask-btn');
    const youtubeUrl = document.getElementById('youtube-url');
    const question = document.getElementById('question');
    const transcriptDiv = document.getElementById('transcript');
    const answerDiv = document.getElementById('answer');
    const qaSection = document.getElementById('qa-section');

    transcribeBtn.addEventListener('click', () => {
        fetch('/transcribe', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: youtubeUrl.value }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                transcriptDiv.textContent = data.transcript;
                qaSection.style.display = 'block';
            }
        });
    });

    askBtn.addEventListener('click', () => {
        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                url: youtubeUrl.value,
                question: question.value 
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                answerDiv.textContent = data.answer;
            }
        });
    });
});
