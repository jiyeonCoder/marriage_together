console.log(":)")


window.addEventListener('load', function () {
    const payload = localStorage.getItem("payload");
    const payload_parse = JSON.parse(payload)
    // console.log(payload_parse.email)

    const intro = document.getElementById("intro")
    intro.innerText = payload_parse.email
})

window.addEventListener('load', async function loadPosts() {
    posts = await getPosts()
    console.log(posts)

    const post_list = document.getElementById("post_list")

    posts.forEach(post => {
        const newItem = document.createElement("div");
        newItem.setAttribute("class", "item")


        const newPolaroid = document.createElement("div")
        newPolaroid.setAttribute("class", "polaroid")
        newPolaroid.setAttribute("id", post.id)

        newItem.appendChild(newPolaroid)

        const postImage = document.createElement("img")
        if (post.image) {
            postImage.setAttribute("src", `${backend_base_url}${post.image}`)
        } else {
            postImage.setAttribute("src", "https://s3-us-west-2.amazonaws.com/s.cdpn.io/210284/l867sBU.jpg")
        }

        newPolaroid.appendChild(postImage)

        const Newmore = document.createElement("details")
        Newmore.setAttribute("class", "more")
        const DetailButton = document.createElement("summary")
        DetailButton.innerText = "포스트 상세보기"
        Newmore.appendChild(DetailButton)

        const comments = post.post_comment.values();
        for (const value of comments) {
            console.log(value.content);
            const newComment = document.createElement("div")
            newComment.setAttribute("class", "comments")
            newComment.innerText = value.content
            Newmore.append(newComment)
        }

        newPolaroid.appendChild(Newmore)







        post_list.appendChild(newItem)

    })
})

