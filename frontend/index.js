console.log(":)")


window.onload = () => {
    const payload = localStorage.getItem("payload");
    const payload_parse = JSON.parse(payload)
    console.log(payload_parse.email)

    const intro = document.getElementById("intro")
    intro.innerText = payload_parse.email
}

function openCloseToc() {
    if (document.getElementById('toc-content').style.display === 'block') {
        document.getElementById('toc-content').style.display = 'none';
        document.getElementById('toc-toggle').textContent = '댓글 보기';
    } else {
        document.getElementById('toc-content').style.display = 'block';
        document.getElementById('toc-toggle').textContent = '숨기기';
    }
}