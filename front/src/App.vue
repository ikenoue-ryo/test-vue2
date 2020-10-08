<div class="imgContent">
          <div class="imagePreview">  
          <img :src="uploadedImage" style="width:100%;" />
             <input type="file" class="file_input" name="photo" @change="onFileChange"  accept="image/*" />
          </div>
        </div>
