document.addEventListener("DOMContentLoaded", function () {
  tinymce.init({
      selector: "#editor",
      height: 500,
      plugins: "advlist autolink lists link image charmap print preview",
      toolbar: "undo redo | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image",
  });

  document.getElementById("save-button").addEventListener("click", function () {
      const editedContent = tinymce.get("editor").getContent();
      console.log("Edited Content:", editedContent);
      alert("Content saved (for now, just logged to console)!");
  });
});
