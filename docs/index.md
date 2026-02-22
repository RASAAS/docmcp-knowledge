---
layout: page
---

<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  const lang = navigator.language?.startsWith('zh') ? 'zh' : 'en'
  window.location.replace('/' + lang + '/')
})
</script>

<noscript>
  <meta http-equiv="refresh" content="0; url=/en/" />
</noscript>
