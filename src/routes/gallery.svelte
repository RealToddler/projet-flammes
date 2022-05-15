<script>
    import { onMount } from 'svelte';

    let Carousel;

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
                "code/picture5.png",
                "code/picture6.png",
                "code/picture7.png",
                "code/picture8.png",
                "code/picture9.png",
                "code/picture10.png",
                "code/picture11.png",
                "code/picture12.png"
            ]
        }
    ];

</script>

<title>PROJET FLAMMES | GALERIE</title>
<div class=" w-screen
    py-5 space-y-5
    bg-rose-600">
    <div class="
        px-1/32">
        <h1 class="
            text-5xl text-white
            font-semibold">
            GALERIE
        </h1>
        <p class="
            text-3xl text-white
            font-normal">
            Retrouvez sur cette page plusieurs photos / captures d'écrans prises 
            tout au long du projet.
        </p>
    </div>
    {#each pictures as picture}
        <div>
            <svelte:component this={Carousel}
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
                    <div class="
                        grid-2">
                        <div class="w-11/12 h-auto
                                rounded 
                                shadow-lg">
                            <img class="
                                    rounded-t
                                    border-gray-800"
                                src="{src}" 
                                alt="">
                            <a href="{src}" 
                                target="_blank">
                                <button class="w-full h-8 
                                            rounded-b
                                            bg-gray-800
                                            hover:bg-sky-600 transition duration-650"
                                        style="outline:none">
                                    <svg xmlns="http://www.w3.org/2000/svg" 
                                        class="h-6 w-6
                                            self-center mx-auto" 
                                        fill="none" 
                                        viewBox="0 0 24 24" 
                                        stroke="white" 
                                        stroke-width="1.5">
                                        <path 
                                            stroke-linecap="round" 
                                            stroke-linejoin="round" 
                                            d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
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