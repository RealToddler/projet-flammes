<script lang="js">
    import ScrollButton from '$lib/components/ScrollButton.svelte'
    import FirstPart from '$lib/components/FirstPart.svelte';
    import SecondPart from '$lib/components/SecondPart.svelte';
</script>

<div id="menu"
    class="min-h-screen min-w-screen max-h-full
        text-white
        flex
        bg-cyan-800">
    <!--UP BUTTON-->
    <div class="h-auto mx-auto">
        <div class="h-1/7
            flex justify-center">
            <ScrollButton direction = {"up"} id = {"problematic"}/>
        </div>
        <!--MENU PART-->
        <div class="h-5/7
            flex justify-center">
            <div class="
                self-center">
                <FirstPart/>
                <SecondPart/>
                <br>
            </div>
        </div>
        <!--DOWN BUTTON-->
        <div class="h-1/7
            flex justify-center self-end">
            <div class="
                self-end">
                <ScrollButton direction = {"down"} id = {"conclusion"}/>
            </div>
        </div>
    </div>
</div>
