function deleteNote(noteId){
console.log(noteId)
    fetch('/delete-errand', {
        method:'POST',
        body: JSON.stringify({ noteId: noteId })
    }).then((_res) => {
        window.location.href = "/"
    });
}