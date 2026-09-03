# 避脸构图参考库

用途：通过摄影构图减少清晰正脸占比，让注意力集中在服装和穿戴场景，降低不自然的人脸细节对画面的影响；不保证生成结果一定真实。

默认优先从下表选择适合商品和场景的一种手法，在营销方案中说明，确认后写入出图Prompt。用户明确要求露脸或看清表情时，不使用避脸策略。

## 手法清单

| 手法 | 说明 | 英文Prompt写法参考 | 适合场景与限制 |
|---|---|---|---|
| 背影/侧背 | 不露正脸，展示背面剪裁、走路姿态 | shot from behind, back view, showing the silhouette and verified back details of the outfit, face not visible | 已有背面参考且背面展示符合营销重点；不能仅凭正面图默认选用 |
| 过肩/侧后方 | 镜头在肩后或侧后方，脸转离镜头 | camera positioned slightly behind the shoulder, face turned away and partially out of frame | 保留人物存在感；须有对应服装视角依据，不遮挡主要卖点 |
| 齐颈/齐下巴取景 | 拍摄时将面部置于画框外，保留身体和服装 | compose directly with the upper frame edge at chin or neck level, focus on the outfit, no visible face | 上衣、外套、连衣裙；保留领口和要求展示的服装长度，不事后裁切成品改变比例 |
| 局部特写 | 展示手部、衣角或面料等已知细节 | close-up detail shot of the verified garment detail, no face in frame | 单品细节或已确认的细节窗口；不能替代用户要求的完整穿搭，不添加未经确认的口袋等设计 |
| 逆光轮廓 | 以逆光弱化面部细节 | backlit figure near a window or doorway, face turned away, soft rim light, garment color and texture remain visible | 氛围、情绪型内容；不要让服装成为黑色剪影而丢失原色、纹理 |
| 行走/转身瞬间 | 自然抓拍，转头或头发局部遮挡面部 | candid mid-stride or turning motion, face turned away, hair partially obscuring facial features, garment details remain sharp | 场景型、动态内容；不靠夸张动作或模糊服装掩盖人脸 |
| 低头/侧转动作 | 整理衣领、看手中物品等自然动作 | head tilted down adjusting the collar, face angled away from the camera, natural candid posture | 通勤、生活化瞬间；轻微低头仍可能露脸，严格不露脸时应选画框外取景或有依据的背影视角 |

## 使用规则

- 在营销方案确认前选择，带字和不带字都适用。带字时与 `layout_composition_guide.md` 的版式搭配；摄影视角与文字版式是不同维度，不必绑定固定组合。
- 商品真实性、完整展示要求和用户指定的镜头优先。不能为了避脸编造背面细节、遮住领口或裁掉裙长。没有合适的避脸方式时，在方案中说明取舍，等用户确认。
- 可见历史中尽量轮换适合的手法，不每次都用背影；不能为轮换牺牲商品展示。多个尺寸延续已确认手法，在各自目标画布内重新排布，不追加图片。
- 避脸不等于沿用原图镜自拍、手机遮脸或只换背景；仍需遵守主技能的全新穿戴场景规则。用户明确要求原图编辑时，不能擅自改变人物姿势来避脸。
- 用户要求“完全不露脸”时，不把侧脸、低头或虚焦当作满足要求；检查面部是否确实位于画框外或完全不可见。
- 用户要求露脸或看清表情时，正常描述脸部与表情，可使用 `natural skin texture, realistic lighting, candid posture, no excessive beauty retouching`，不要承诺仅靠Prompt消除人脸失真。
- 情绪型内容可通过姿态、步伐和场景互动表达情绪，例如 `confident posture, relaxed walking pace`。如果文案必须依赖清晰表情，在确认方案中说明露脸的理由，不暗中改变用户选择。
