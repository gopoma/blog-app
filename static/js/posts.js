function showDeleteConfirmation(id) {
    const response = confirm("Are you shure?");
    if(response) {window.location.href = `/posts/delete/${id}`;}
}