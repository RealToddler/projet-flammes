<script>
    export let shown = false
    export const show = () => { shown = !shown }

    export let shown2 = false
    export const show2 = () => { shown2 = !shown2 }

    export let shown3 = false
    export const show3 = () => { shown3 = !shown3 }
  </script>
  
{#if shown}
    <slot/>
{/if}

{#if shown2}
    <slot/>
{/if}

{#if shown3}
    <slot/>
{/if}
