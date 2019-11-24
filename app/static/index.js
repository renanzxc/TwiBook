function sendPost(){
    var form_data = new FormData();
    var form = document.getElementById('post-form');
    form_data.createdBy = parseInt(form[0].value)
    form_data.title = form[1].value
    form_data.text = form[2].value
    console.log(form_data)
    document.getElementById('post-form')[1].value = ''
    document.getElementById('post-form')[2].value = ''

    axios.post("/insere_post",{
        form_data
    }).then(response => {
        if(response.data.status == '1'){
            var element = document.getElementById('list-posts');
            element.innerHTML = '<br>'+
            `<div class="card gedf-card" id="post ${response.data.post.id}">`+
              `<input type="hidden" id="likedBy" value="LikedBy">`+
                '<div class="card-header">'+
                    '<div class="d-flex justify-content-between align-items-center">'+
                        '<div class="d-flex justify-content-between align-items-center">'+
                            '<div class="mr-2">'+
                                '<img class="rounded-circle" width="45" src="https://picsum.photos/50/50" alt="">'+
                            '</div>'+
                            '<div class="ml-2">'+
                                `<div class="h5 m-0">${response.data.post.user.username}</div>`+
                                `<div class="h7 text-muted">${response.data.post.user.name}</div>`+
                            '</div>'+
                        '</div>'+
                        '<div>'+
                            '<div class="dropdown">'+
                                '<button class="btn btn-link dropdown-toggle" type="button" id="gedf-drop1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'+
                                    '<i class="fa fa-ellipsis-h"></i>'+
                                '</button>'+
                                '<div class="dropdown-menu dropdown-menu-right" aria-labelledby="gedf-drop1">'+
                                    '<div class="h6 dropdown-header">Configuration</div>'+
                                    '<a class="dropdown-item" href="#">Save</a>'+
                                    '<a class="dropdown-item" href="#">Hide</a>'+
                                    '<a class="dropdown-item" href="#">Report</a>'+
                                '</div>'+
                            '</div>'+
                        '</div>'+
                    '</div>'+

                '</div>'+
                '<div class="card-body">'+
                    '<div class="text-muted h7 mb-2"> <i class="fa fa-clock-o"></i>10 min atrás</div>'+
                    '<a class="card-link" href="#">'+
                        `<h5 class="card-title">${form_data.title}</h5>`+
                    '</a>'+
''+
                    '<p class="card-text">'+
                        `${form_data.text}`+
                    '</p>'+
                '</div>'+
                '<div class="card-footer">'+
                    `<a href="javascript:likePost('post ${response.data.post.id}')"  id="buttonLike" class="card-link like">  <i class="fa fa-gittip"></i> Curtir</a>`+
                    '<a href="#" class="card-link"><i class="fa fa-comment"></i> Comentar</a>'+
                    '<a href="#" class="card-link"><i class="fa fa-mail-forward"></i> Compartilhar</a>'+
                '</div>'+
            '</div>'+element.innerHTML
        }
    })

}

function likePost(postId){
    // console.log(buttonLike.style.color)

    
    var form_data = new FormData();
    form_data.liked_post = parseInt(postId.split(" ")[1])
    //form_data.numLikes = parseInt(numLikes)
    form_data.liked_by = parseInt(document.getElementById("idUser").value)
    axios.post("/like_post",{form_data}).then(response => {
      if(response.data.status == '1'){
        let buttonLike = document.getElementById(postId).getElementsByClassName("like")[0]
        let numLikes = parseInt(buttonLike.text.split(" ")[0])

        if(response.data.action == 'like'){
            buttonLike.style.color = "red"
            if(Number.isInteger(numLikes)){
                buttonLike.innerHTML = numLikes+1 + ' <i class="fa fa-gittip"></i> Curtir'
            }
            else{
                buttonLike.innerHTML = '1 <i class="fa fa-gittip"></i> Curtir'
            }
        }
        else if(response.data.action == 'dislike'){
            buttonLike.style.color = "#007bff"

            if(numLikes-1 == 0){  //Se zerar deixa vazio
                buttonLike.innerHTML = '  <i class="fa fa-gittip"></i> Curtir'
            }else{
                buttonLike.innerHTML = numLikes-1 + ' <i class="fa fa-gittip"></i> Curtir'
            }
        }

      }else if(response.data.status == '2'){
        console.log(response.data.error)
      }
    })
}

function focusComment(postId){
    document.getElementById(postId).getElementsByClassName("commentInput")[0].focus()
}

function deletePost(postId){
    axios.delete("/delete_post/"+parseInt(postId.split(" ")[1])).then(response => {
        if(response.data.status == '1'){
            document.getElementById(postId).remove()
        }
    })
}

function commentPost(postId){
    var form_data = new FormData();
    form_data.created_by = parseInt(document.getElementById("idUser").value)
    form_data.text = document.getElementById('commentInput').value
    document.getElementById('commentInput').value = ''
    axios.post("/comment_post/"+parseInt(postId.split(" ")[1]),{form_data}).then(response => {
        if(response.data.status == '1'){
            let element = document.getElementById(postId).getElementsByClassName("comments")
            element[0].innerHTML = element[0].innerHTML+
            '<div class="card bg-light bg-primary" >'+
              '<div class="card-header font-weight-bold comment-header '+
              `">${response.data.comment.user.username}</div>`+
              '<div class="card-body comment-body">'+                        
                `<p class="card-text">${response.data.comment.text}</p>`+
              '</div>'+
            '</div>'
        }
    })
}