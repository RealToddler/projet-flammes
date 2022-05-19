<script lang="js">
    import ScrollButton from '$lib/components/ScrollButton.svelte';
</script>

<div id="conclusion"
    style="background-image: url(menu-pics/???.png); 
        background-repeat: no-repeat; 
        background-position: center; 
        background-size: cover">
    <div class="h-screen">
        <!--UP BUTTON-->
        <div class="h-1/7 
            flex justify-center">
                <ScrollButton direction = {"up"} id = {"menu"}/>
        </div>
        <div class="h-5/7 
            flex justify-center">
            <div class="
                flex self-center 
                rounded-xl border-3">
                <h1 class="self-center py-5 px-5
                    text-white text-5xl text-center 
                    font-semibold">
                    CONCLUSION
                </h1>
            </div>
        </div>
    </div>
</div>

<!--BACKGROUND VIDEO-->
<video id="background-video"
    class="h-screen w-screen"
    autoplay 
    loop 
    muted = {true}
    poster="flames/picture4.png">
    <source src="flames/video_flames.mp4" 
        type="video/mp4">
  </video>

<style>      
    #background-video {
        object-fit: cover;
        position: fixed;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        z-index: -1;
        }
  </style>