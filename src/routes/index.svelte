<script>
    import * as animateScroll from "svelte-scrollto";
</script>

<!--Problématique-->
<div id="pbq"
    style="background-image: url(backgrounds/index_pbq_bg.png); background-repeat: no-repeat; 
        background-position: top; background-size: cover">
    <div class="h-screen select-none">
        <div class="h-1/2 flex">
            <div class="flex self-center mx-auto h-50 w-175 
                rounded-lg border-4 shadow-2xl shadow-white">
                <h1 class="text-center self-center text-4xl text-white font-semibold">
                    A QUOI SONT LIEES LES COULEURS DES FLAMMES ?
                </h1>
            </div>
        </div>
        <div class="h-1/2 flex">
            <div class="self-end mx-auto">
                <button on:click={() => animateScroll.scrollTo({element: '#part1', duration: 2000})}
                class="h-12 w-20 bg-gray-200 rounded-t-4xl flex hover:bg-gray-400
                transition duration-650"
                style="outline:none;">
                    <div class="self-center mx-auto animate-bounce 
                        hover:animate-none">
                        <svg xmlns="http://www.w3.org/2000/svg" 
                        class="h-6 w-6 hover:stroke-white" fill="none" 
                        viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                            <path stroke-linecap="round" 
                                stroke-linejoin="round" d="M19 13l-7 7-7-7m14-8l-7 7-7-7" />
                        </svg>
                    </div>
                </button>
            </div>
        </div>
    </div>
</div>
<!--1ere Partie-->
<div id="part1">
    <div class="h-screen select-none">
        <div class="h-1/2 flex">
            <div class="self-start mx-auto">
                <button on:click={() => animateScroll.scrollTo({element: '#pbq', duration: 2000})}
                class="h-12 w-20 bg-gray-200 rounded-b-4xl flex hover:bg-gray-400
                transition duration-650"
                style="outline:none;">
                    <div class="self-center mx-auto animate-bounce 
                        hover:animate-none">
                        <svg xmlns="http://www.w3.org/2000/svg" 
                        class="h-6 w-6 hover:stroke-white" fill="none" 
                        viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                            <path stroke-linecap="round" 
                                stroke-linejoin="round" d="M5 11l7-7 7 7M5 19l7-7 7 7" />
                          </svg>
                    </div>
                </button>
            </div>
        </div>
        <div class="h-1/2 flex">
            <div class="self-end mx-auto">
                <button on:click={() => animateScroll.scrollTo({element: '#pbq', duration: 2000})}
                class="h-12 w-20 bg-gray-200 rounded-t-4xl flex hover:bg-gray-400
                transition duration-650"
                style="outline:none;">
                    <div class="self-center mx-auto animate-bounce 
                        hover:animate-none">
                        <svg xmlns="http://www.w3.org/2000/svg" 
                        class="h-6 w-6 hover:stroke-white" fill="none" 
                        viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                            <path stroke-linecap="round" 
                                stroke-linejoin="round" d="M19 13l-7 7-7-7m14-8l-7 7-7-7" />
                        </svg>
                    </div>
                </button>
            </div>
        </div>
    </div>
</div>

<style>
</style>
