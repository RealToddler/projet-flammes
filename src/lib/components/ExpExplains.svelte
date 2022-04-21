<script>
    export let shown1 = false
    export const show1 = () => { shown1 = !shown1 }
    export let shown11 = false
    export const show11 = () => { shown11 = !shown11 }
    export let shown12 = false
    export const show12 = () => { shown12 = !shown12 }

    export let shown2 = false
    export const show2 = () => { shown2 = !shown2 }
    export let shown21 = false
    export const show21 = () => { shown21 = !shown21 }
    export let shown22 = false
    export const show22 = () => { shown22 = !shown22 }
  </script>
  
{#if shown1}
    <slot/>
{/if}

{#if shown11}
    <slot/>
{/if}

{#if shown12}
    <slot/>
{/if}

{#if shown2}
    <slot/>
{/if}

{#if shown21}
    <slot/>
{/if}

{#if shown22}
    <slot/>
{/if}
