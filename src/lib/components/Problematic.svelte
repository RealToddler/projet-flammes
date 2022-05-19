<script lang="js">
    import ScrollButton from '$lib/components/ScrollButton.svelte';
</script>

<div id="problematic"
    style="background-image: url(flames/picture4.png); 
        background-repeat: no-repeat; 
        background-position: center; 
        background-size: cover">
    <div class="h-screen w-screen">
        <div class="h-6/7 
            flex justify-center">
            <div class="
                flex justify-center ">
                <h1 class="
                    self-center py-5 px-5
                    text-white text-5xl text-center 
                    font-semibold
                    rounded-xl border-3">
                    A QUOI SONT LIEES <br>LES COULEURS DES FLAMMES ?
                </h1>
            </div>
        </div>
        <div class="h-1/7 
            flex justify-center">
            <div class="
                self-end">
                <ScrollButton direction = {"down"} id = {"menu"}/>
            </div>
        </div>
    </div>
</div>