<script>
    import { onMount } from 'svelte';

    let Carousel; // for saving Carousel component class
    let carousel; // for calling methods of the carousel instance

    onMount(async () => {
        const module = await import('svelte-carousel');
        Carousel = module.default;
    });

    const pictures = [
        {
            direction: "next",
            src: [
                "flames/picture1.png",
                "flames/picture2.png",
                "flames/picture3.png",
                "flames/picture4.png",
                "flames/picture5.png",
                "flames/picture6.png",
                "flames/picture7.png"
            ]
        },
        {
            direction: "prev",
            src: [
                "protocol/picture1.png",
                "protocol/picture2.png",
                "protocol/picture3.png",
                "protocol/picture4.png"
            ]
        },
        {
            direction: "next",
            src: [
                "code/picture1.png",
                "code/picture2.png",
                "code/picture3.png",
                "code/picture4.png",
                "code/picture5.png"
            ]
        }
    ];

</script>

<div class="py-5 space-y-5 select-none"
    style="background-image: url(backgrounds/gallery_bg.png); background-repeat: no-repeat;   
    background-position: 1/2; background-size: cover">>
    <div class="ml-1/16">
        <h1 class="text-xl font-light text-white">
            Retrouvez sur cette page plusieurs photos / captures d'écrans prises 
            tout au long du projet.
        </h1>
    </div>
    {#each pictures as picture}
        <div>
            <svelte:component this={Carousel} bind:this={carousel}
                arrows = {false}
                dots = {false}
                swiping = {false}
                particlesToShow = {4}
                particlesToScroll = {1}
                duration = {5000}
                autoplay = {true}
                autoplayDuration = {1}
                autoplayDirection = {picture.direction}
                autoplayProgressVisible = {false}
                timingFunction = {'linear'}>
                {#each picture.src as src}
                    <div class="grid-2 main">
                        <div class="w-110 h-auto shadow-lg">
                            <img src="{src}" alt="" class="rounded-t 
                            border-l-3 border-r-3 border-t-3 border-gray-800">
                            <a href="{src}" target="_blank">
                                <button class="w-full bg-gray-800 h-8 rounded-b
                                hover:bg-gray-600 transition duration-650"
                                style="outline:none">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 self-center mx-auto" fill="none" viewBox="0 0 24 24" stroke="white" stroke-width="1.5">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                    </svg>
                                </button>    
                            </a>
                        </div>
                    </div>
                {/each}
            </svelte:component>
        </div>
    {/each}  
</div>

<style>
</style>