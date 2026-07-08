import DefaultTheme from 'vitepress/theme'
import './custom.css'
import FeatureBoard from './components/FeatureBoard.vue'
import DiscussionWall from './components/DiscussionWall.vue'
import type { Theme } from 'vitepress'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('FeatureBoard', FeatureBoard)
    app.component('DiscussionWall', DiscussionWall)
  },
} satisfies Theme
