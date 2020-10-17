<template>
  <div>
      <input @change="selectedFile" type="file" name="file">
      <!-- <input v-model="title" style="border: 1px solid;">
      <input v-model="content" style="border: 1px solid;"> -->
      <button @click="upload">送信</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return{
      uploadFile: null,
      picture: '',
      // title: '',
      // content: '',
    }
  },
  methods: {
    selectedFile: function(e) {
        e.preventDefault();
        let files = e.target.files;
        this.uploadFile = files[0];
        console.log('uploadFile', this.uploadFile)
    },
    upload: function() {
        let formData = new FormData();
        formData.append('picture', this.uploadFile);
        let config = {
            headers: {
                'content-type': 'multipart/form-data'
            }
        };
        console.log('formData', formData)
        axios
            .post('http://127.0.0.1:8000/api/v1/posts/create/', formData, config)
            .then(function(response) {
                console.log(response)
            })
            .catch(function(error) {
                console.log(error)
            })
    }
}
}
</script>