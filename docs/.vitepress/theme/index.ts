import DefaultTheme from 'vitepress/theme'
import './custom.css'
import FeatureBoard from './components/FeatureBoard.vue'
import DiscussionWall from './components/DiscussionWall.vue'
import ReguverseHub from './components/ReguverseHub.vue'
import type { Theme } from 'vitepress'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('FeatureBoard', FeatureBoard)
    app.component('DiscussionWall', DiscussionWall)
    app.component('ReguverseHub', ReguverseHub)
  },
} satisfies Theme
