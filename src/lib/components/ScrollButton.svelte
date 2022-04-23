<script lang="js">
    import * as animateScroll from 'svelte-scrollto';
    export let direction, id;
</script>


{#if direction == 'down'}
    <div>
        <button on:click={() => animateScroll.scrollTo({element: '#'+id, duration: 2000})}
            class="h-12 w-20 
                flex
                rounded-t-4xl
                bg-gray-200 
                hover:bg-gray-400 transition duration-650"
            style="outline:none;">
                <div class="
                    self-center mx-auto 
                    animate-bounce 
                    hover:animate-none">
                    <svg xmlns="http://www.w3.org/2000/svg" 
                        class="h-6 w-6 
                            hover:stroke-white" 
                        fill="none" 
                        viewBox="0 0 24 24" 
                        stroke="black" 
                        stroke-width="1.5">
                        <path stroke-linecap="round" 
                            stroke-linejoin="round" 
                            d="M19 13l-7 7-7-7m14-8l-7 7-7-7" />
                    </svg>
                </div>
        </button>
    </div>
{:else if direction == 'up'}
    <div>
        <button on:click={() => animateScroll.scrollTo({element: '#'+id, duration: 2000})}
            class="h-12 w-20 
                flex 
                rounded-b-4xl 
                bg-gray-200 
                hover:bg-gray-400 transition duration-650"
            style="outline:none;">
                <div class="
                    self-center mx-auto 
                    animate-bounce 
                    hover:animate-none">
                    <svg xmlns="http://www.w3.org/2000/svg" 
                        class="h-6 w-6 
                            hover:stroke-white" 
                        fill="none" 
                        viewBox="0 0 24 24"
                        stroke="black"
                        stroke-width="1.5">
                        <path stroke-linecap="round" 
                            stroke-linejoin="round" 
                            d="M5 11l7-7 7 7M5 19l7-7 7 7" />
                    </svg>
                </div>
        </button>
    </div>
{/if}
